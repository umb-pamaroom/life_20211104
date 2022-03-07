

$(document).ready(function() {
    
        // Drag and drop mechanics
        function init_drag_and_drop_mechanics(){
            $('.card-reactor').draggable({
                helper: 'clone',
                containment: ".inner-wrap",
                start  : function(event, ui){
                    $(ui.helper).addClass("ui-helper");
                     $(this).draggable('instance').offset.click = {
                        // This helps the draggable instance to be in
                        //      the center of the cursor.
                        left: Math.floor(ui.helper.width() / 2),
                        top: Math.floor(ui.helper.height() / 2)
                    }; 
                }

            });

            $('.list-box').droppable({
                tolerance: "touch",
                drop: function(event, ui){
                    var card_id= $(ui.draggable).data("card_id");
                    var to_column_id = $(this).data("value");
                    var from_column_id = $(ui.draggable).data('value');
                    var url = $("#hidden-transfer-cards").data("url");
                    data = {
                        card_id : card_id,
                        to_column_id : to_column_id,
                        from_column_id : from_column_id
                    }
                    $.post(url,data,reload_inner_wrapper,'json'), function(err){

                    };
                }
            });
        }

        init_drag_and_drop_mechanics();
        // using jQuery
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        var csrftoken = getCookie('csrftoken');
        

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        // Animations
        $(document).on("click", '#btnRemove', function(){
            // Sequence of prompting and error of removing members
            var atLeastOneIsChecked = $('input[name="remove_member"]:checked').length > 0;
            if (atLeastOneIsChecked==true) {
                $("#reactor").empty();
                $('#RemoveMemberModal').modal('hide');
                $('#RemoveConfirmationModal').modal('show');
            }else{
                $('#RemoveConfirmationModal').modal('hide');
                $("#reactor").html('<label id="label_error"\
                class="alert alert-block alert-danger lbl_margin">\
                Please check at least one checkbox to remove!</label>');
            }
        });

        $('#RemoveConfirmationModal').on('hidden.bs.modal', function () {
                $('#RemoveMemberModal').modal('show');
        })


        $(document).on("click", '.ClassEditComment', function(){
                card_id=$(this).data('value');
                console.log(card_id);
                $('#DivisionComment-'+card_id).addClass('display-none');
                $('#InputComment-'+card_id).removeClass('display-none');
                $('#EditComment-'+card_id).addClass('display-none');
                $('#DeleteComment-'+card_id).addClass('display-none');
                $("#card-save-button-"+card_id).removeClass('display-none');
                $("#card-cancel-button-"+card_id).removeClass('display-none');
        })

         $(document).on("click", '.class-card-cancel-button', function(){
                card_id=$(this).data('value');
                console.log(card_id);
                $('#DivisionComment-'+card_id).removeClass('display-none');
                $('#InputComment-'+card_id).addClass('display-none');
                $('#EditComment-'+card_id).removeClass('display-none');
                $('#DeleteComment-'+card_id).removeClass('display-none');
                $("#card-save-button-"+card_id).addClass('display-none');
                $("#card-cancel-button-"+card_id).addClass('display-none');
        })



        $('#DeleteCommentModal').on('hidden.bs.modal', function () {
                $('#CardModal').modal('show');
        })

        $('#CardMemberModal').on('hidden.bs.modal', function () {
                $('#CardModal').modal('show');
        })

        $('#ArchiveCardConfirmation').on('hidden.bs.modal', function () {

            console.log($(this).data('hide'));
            if($(this).data('hide')=="yes"){
                $(this).data('hide','no');
                $('#CardModal').modal('hide');
            }else{

                $('#CardModal').modal('show');
            }

        })

        $('#DueDateModal').on('hidden.bs.modal', function () {
                $('#CardModal').modal('show');
        })

        if ($('div.error-box-index').length) {
             $('#createBoardModal').modal('show');
        }

        if ($('div.error-box-boards').length) {
             $('#EditBoardModal').modal('show');
        }

        if ($('div.error-box-member-invite').length) {
             $('#AddMemberModal').modal('show');
        }

        if ($('#MessageBoxModalAlert').length) {
             $('#MessageBoxModalAlert').modal('show');
        }
        

        
        // Adding a column animation
        $(document).on("click", '.add-input-reactor', function(){
            $(".add-input-reactor").hide();
            $("#list-form").show();
            $( "#list-form > input" ).focus();
        });

        $(document).on("click", '.close-add-list', function(){
            $("#list-form").hide();
            $(".add-input-reactor").show();
        });

        $(document).on("blur", '#list-form > input', function(){
            // Losing focus on text input
            if (!$(this).val().length) {
                $("#list-form").hide();
                $(".add-input-reactor").show();
            }
        });


        $(document).on("click", '.title-card-class', function(){
            value = $(this).data('value');
            $(".add-card-reactor-"+value).hide();
            $("#card-add-form-column-"+value).show();
            $( "#add-card-reactor-"+value+" > input" ).focus();
        });

        $(document).on("click", '#close-add-card', function(){
            value = $(this).data('value');
            $("#card-add-form-column-"+value).hide();
            $(".add-card-reactor-"+value).show();
        });

        // Existing Columns Animation
        $(document).on("dblclick", '.existing-label', function(){
            id=$(this).data('value');
            $("#existing-label-"+id).hide();
            $("#existing-form-"+id).show();
            $( "#existing-form-"+id+" > input" ).focus();
        });

        $(document).on("click", '.existing-form', function(){
            id=$(this).data('value');
            $("#existing-form-"+id).hide();
            $("#existing-label-"+id).show();
        });

        // Decsription Animation
        $(document).on("dblclick", "#text-id-description", function(){
            if($('#text-id-description').prop('readonly')){

               $('#text-id-description').attr("readonly",false);
               $("#card-button-add-description").removeClass('display-none');
               $("#card-button-cancel-description").removeClass('display-none');
               $( "#hr-after-description" ).addClass( "mt-4" );
            }
        });
        $(document).on("click", "#card-button-cancel-description", function(){
          $('#text-id-description').attr("readonly",true);
          $("#card-button-add-description").addClass('display-none');
          $("#card-button-cancel-description").addClass('display-none');
          $( "#hr-after-description" ).removeClass( "mt-4" );
        });

        // Comment Animation
        $(document).on("click", "#text-comment-area", function(){
            $("#card-button-add-comment").removeClass('display-none');
            $("#card-button-cancel-comment").removeClass('display-none');
           
          });
        $(document).on("click", "#card-button-cancel-comment", function(){
          $("#card-button-add-comment").addClass('display-none');
          $("#card-button-cancel-comment").addClass('display-none');
        });

        // Animation for card title
        $(document).on("click", "#heading-card-title", function(){
          $("#heading-card-title").addClass('display-none');
          $("#input-card-title").removeClass('display-none');
          $("#card-button-update-title").removeClass('display-none');
          $("#card-button-cancel-title").removeClass('display-none');
          $("#input-card-title").focus();
        });

        
        $(document).on("click", "#card-button-cancel-title", function(){
          $("#heading-card-title").removeClass('display-none');
          $("#input-card-title").addClass('display-none');
          $("#card-button-update-title").addClass('display-none');
          $("#card-button-cancel-title").addClass('display-none');
        });

        $(document).on("click", "#card-button-update-title", function(){
            $("#heading-card-title").removeClass('display-none');
            $("#input-card-title").addClass('display-none');
            $("#card-button-update-title").addClass('display-none');
            $("#card-button-cancel-title").addClass('display-none');

            url=$('#heading-card-title').attr('action');
            id =$('#heading-card-title').data('card_id');
            var title=$('#input-card-title').val();
            if (title){
                data = {
                    title : title,
                    card_id : id
                }

                $.post(url,data,reload_card_title,'json'), function(err){
                    console.log("error");
                };
            }
        });

        $(document).on("blur", "#input-card-title", function(){
          $("#input-card-title").addClass('display-none');
          $("#heading-card-title").removeClass('display-none');
        });



        function formatDate(date) {
            var year = date.getFullYear(),
                month = date.getMonth() + 1, 
                day = date.getDate(),
                hour = date.getHours(),
                minute = date.getMinutes(),
                second = date.getSeconds(),
                hourFormatted = hour % 12 || 12, 
                minuteFormatted = minute < 10 ? "0" + minute : minute,
                morning = hour < 12 ? "am" : "pm";

            return month + "/" + day + "/" + year + ", " + hourFormatted + ":" +
                    minuteFormatted + morning;
        }

        function zero_padding(val) {
            // padding for date month
            // date time local doesn't accept '7' -> must be '07'
          if (val >= 10)
            return val;
          else
            return '0' + val;
        }

        function format_date_for_input(date) {
            var year = date.getFullYear(),
                month = date.getMonth() + 1, 
                day = date.getDate(),
                hour = date.getHours(),
                minute = date.getMinutes(),
                second = date.getSeconds(),
                hourFormatted = hour % 12 || 12, 
                minuteFormatted = minute < 10 ? "0" + minute : minute,
                morning = hour < 12 ? "am" : "pm";

                month = zero_padding(month);
                hour = zero_padding(hour);


            return year + "-" + month + "-" + day + "T" + hour + ":" +
                    minuteFormatted;
        }


        // Ajax Calls
        $(document).on('submit','#list-form', function(e){
            e.preventDefault()
            var title = $('#add-list').val()
            data = {
                title : title
            }
            var url = $(this).attr('action');
            $.post(url,data,reload_inner_wrapper,'json'), function(err){

            };
        });



        $(document).on('submit','.existing-form', function(e){
            e.preventDefault();
            id=$(this).data('value');
            var title = $('#exist-list-' + id).val();
            data = {
                title : title,
                id : id
            }
            var url = $(this).attr('action');

            if (url == undefined){
                url = $('#hidden-column-update-values').val();
            }
            $.post(url,data,reload_inner_wrapper,'json'), function(err){

            };
        });


        $(document).on('submit','#archive-form', function(e){
            e.preventDefault()
            $("#ArchiveColumnModal").data('value',$(this).data('value'));
            $("#ArchiveColumnModal").data('action',$(this).data('action'));
            $("#ArchiveColumnModal").modal("show");
        });

        $(document).on('click','#archived-column-yes', function(e){
            e.preventDefault();

            id=$('#ArchiveColumnModal').data('value');
            var url = $('#ArchiveColumnModal').data('action');

            data = {
                id : id
            }
            if (url == undefined){
                url = $('#hidden-column-archive-values').val();
            }
             $("#ArchiveColumnModal").modal("hide");
            $.post(url,data,reload_inner_wrapper,'json'), function(err){

            };
        });

        pop_members = function(data){

            $('.assign-division input').each(function () {
                console.log(this.value);
                card_member = JSON.parse(data.card_member);
                var count = 0;
                var checked = false;
                while(count < card_member.length){
                    console.log(card_member);
                    console.log(card_member[count].fields.board_member);
                    if(card_member[count].fields.board_member == this.value){

                        $(this).prop('checked', true);
                        checked = true;
                    }
                    count+=1;
                }
                if(checked==false){
                        $(this).prop('checked', false);
                }
            });
        }

        $(document).on('click','#pop-assign-members', function(e){
            e.preventDefault();
            card_id =$('#heading-card-title').data('card_id');
            url = $('#hidden-get-assigned-members').data('url');
            data = {
                card_id : card_id
            }

            $.get(url,data, pop_members,'json') 
            .fail(function(err){
                console.log(err);
             })


        });


        successful_archive = function(data){
            $('#ArchiveCardConfirmation').modal('hide');
            reload_inner_wrapper(data);
            $('#ArchiveCardConfirmation').data('hide','yes');
        }

        $(document).on('click','#archive-card-confirmation', function(e){
            e.preventDefault();
            card_id =$('#heading-card-title').data('card_id');
            url=$(this).data('url');
            data = {
                card_id : card_id
            }
             $.post(url,data,successful_archive ,'json') 
            .fail(function(err){
                console.log(err);
             })

        });

          $(document).on('click','#set-due-date', function(e){
            // Setting Due Date
            e.preventDefault();
            card_id =$('#heading-card-title').data('card_id');
            date =$('#input-due-date').val();
            console.log(date);
            url = $('#hidden-get-due-date').data('url');
            data = {
                card_id : card_id,
                due_date : date
            }

            $.post(url,data, null
                ,'text') 
            .done(function() {
                $('#CardModal').modal('show');
                $('#DueDateModal').modal('hide');
                reload_board_stream();
              })
            .fail(function(err){
                console.log(err);
             })
        });


        pop_due_date = function(data){
            console.log(data);
            card = JSON.parse(data.card);
            if (card[0].fields.due_date != null){
                to_set = new Date(card[0].fields.due_date);
                to_set = format_date_for_input(to_set);
                // Vanilla Java Script
                console.log(to_set);
                $("#input-due-date").val(to_set);
                
            }else{
                 $("#input-due-date").val(null);
            }
        }

        $(document).on('click','#pop-due-date', function(e){
            e.preventDefault();
            card_id =$('#heading-card-title').data('card_id');
            url = $('#hidden-get-due-date').data('url');

            data = {
                card_id : card_id
            }

            $.get(url,data, pop_due_date,'json') 
            .fail(function(err){
                console.log(err);
             })


        });
        $(document).on('click','#btnAssignRemove', function(e){
            // Assingning and removing a member
            e.preventDefault()
            $('#CardMemberModal').modal('hide');
            var selected = [];
            $('.assign-division input:checked').each(function() {
                selected.push($(this).attr('value'));
            });
            var not_selected = [];
            $('.assign-division input:checkbox:not(:checked)').each(function() {
                not_selected.push($(this).attr('value'));
            });

            card_id =$('#heading-card-title').data('card_id');

            data = {
                not_selected : not_selected,
                selected : selected,
                card_id : card_id
            }
            console.log(data);
            var url = $(this).data('action');
                
            $.post(url,data,reload_card,'json'), function(err){
                console.log('error');
            };
        });

        $(document).on('submit','.card-add-form-class', function(e){
            e.preventDefault()
            id=$(this).data('value');
            name = $("#add-card-"+id).val();
            data = {
                name : name,
                id : id
            }

            console.log("addd");
            var url = $('.card-add-form-class').attr('action');
            if (url == undefined){
                url = $('#hidden-card-add-values').val();
            }
            if(name.length){
                $.post(url,data,reload_inner_wrapper,'json'), function(err){
                    console.log('error');
                };
            }

        });

        // Card Ajax
        $(document).on("click", '.card-reactor', function(){
            // Loading card values to modal
            card_id = $(this).data('card_id');
            data = {
              card_id : card_id
            }

            console.log(card_id);
             var url = $('#hidden-get-card-action').data('url');
             console.log(url);
             $.get(url,data,reload_card,'json') .fail(function(err){
                console.log(err);
             })

        });

        $(document).on("click", '.class-delete-comment', function(){
            // Loading delete value to modal
            value = $('.class-delete-comment').data('value');
            console.log(value + " to_delete");
            $('#delete-comment-yes').data('to_remove',value);
        });

        $(document).on("click", '#delete-comment-yes', function(){
            // Deleting a comment
            $('#DeleteCommentModal').modal('hide');
            id=$('#delete-comment-yes').data('to_remove');
            url =$('#delete-comment-yes').data('url');
            card_id =$('#heading-card-title').data('card_id');
            console.log(id);
            var title=$('#input-card-title').val();
            if (title){
                    data = {
                        comment_id : id,
                        card_id : card_id
                    }

                    $.post(url,data,reload_card,'json')
                    .fail(function(err){
                        console.log(err);
                    })
            }
        });



        // Saving changes for card description
        $(document).on("click", "#card-button-add-description", function(){
            $('#text-id-description').attr("readonly",true);
            $("#card-button-add-description").addClass('display-none');
            $("#card-button-cancel-description").addClass('display-none');
            $( "#hr-after-description" ).removeClass( "mt-4" );
            var id = $('#heading-card-title').data('card_id');
            var description=$('#text-id-description').val();
            var url=$('#hidden-column-update-description').data('url');
            data = {
                description : description,
                card_id : id
            }
            $.post(url,data,null,'text'), function(err){
            };
        });

    
        // Getting the board
        function get_board(){
            url=$("#hidden-column-get-board").data('url')
            $.get(url,null,reload_inner_wrapper,'json'), function(err){
                console.log("error");
            };
        }

        // Reloading Board Stream
        reload_board_stream = function(data){

            url = $('#hidden-activity').data('url');
            $.get(url)
            .done(function(response) {
               $('.sidebar-body').html(response);
            });

        }
        // Html population Region
        reload_card_title = function(data){
           $('.reload-title').empty();
           cards = JSON.parse(data.cards);
           html = cards[0].fields.name;
           $(".reload-title").append(html);
           get_board();
           reload_board_stream(data);

        }

        // Adding Comment
        $(document).on("click","#card-button-add-comment", function(){
            $("#card-button-add-comment").addClass('display-none');
            $("#card-button-cancel-comment").addClass('display-none');

            url=$('#hidden-comment-add').data('url');
            id =$('#heading-card-title').data('card_id');
            var comment=$('#text-comment-area').val();
            data = {
                comment : comment,
                card_id : id
            }
            $.post(url, data, reload_comments,'json') 
            .fail(function() {
                console.log("error");
             })
            $("#text-comment-area").val("");

        });

        reload_comments = function(data){
            $('.comment-reactor').empty();
            comments = JSON.parse(data.comments);
            console.log(data);
            console.log(comments);

            html = "";
            if(comments){
                html += '<!-- Comments -->'
                 +'      <div class="left-portion-of-header col-lg-12 col-md-12 col-sm-12">'
                 +'           <hr class="hr">'
                +'       </div>'
                 +'      <div class="left-portion-of-header col-lg-9 col-md-9 col-sm-9">'
                 +'            <h5 class="modal-card-add-comment" id="exampleModalLabel">Comments</h5>'
                 +'     </div>';
            }
                    
            index = 0;
            while(index < comments.length){
                date_commented = new Date(comments[index].fields.date_commented);
                date_commented = formatDate(date_commented);
                html +='      <!-- To Loop -->'
                     +'       <div class="left-portion-of-header col-lg-12 col-md-12 col-sm-12">'
                     +'            <hr class="hr">'
                     +'       </div>'
                     +'         <div class="left-portion-of-header col-lg-9 col-md-9 col-sm-9">'

                     +'             <p class="card-comment-user" id="exampleModalLabel"><strong>'+comments[index].fields.user+'</strong> ('+date_commented+')</p>'
                     +'             '
                     +'             <div  id="DivisionComment-'+comments[index].pk+'" class="card-comments" name="" novalidate="">'+comments[index].fields.comment+'</div>'
                     +'             <textarea id="InputComment-'+comments[index].pk+'" class="textarea card-comments display-none class-input-comment">'+comments[index].fields.comment+'</textarea>'


                    if(user.current_user==comments[index].fields.user){
                         html+=' <!-- <button data-value="'+comments[index].pk+'" id="EditComment-'+comments[index].pk+'" class="ClassEditComment float-left additional-option-comment link-style btn btn-warning">Edit</button> -->'
                         +'             <button data-value="'+comments[index].pk+'" data-toggle="modal" data-target="#DeleteCommentModal" id="DeleteComment-'+comments[index].pk+'" class="class-delete-comment float-left additional-option-comment link-style btn btn-danger" data-dismiss="modal">Delete</button>'
                         +'           <button data-value="'+comments[index].pk+'" name="" id="card-save-button-'+comments[index].pk+'" class="btn btn-secondary card-button-add-comment mt-1 float-right display-none">Save</button>'
                         +'           <button data-value="'+comments[index].pk+'" name="" id="card-cancel-button-'+comments[index].pk+'" class="class-card-cancel-button btn btn-secondary card-button-add-comment mr-2 mt-1 float-right display-none">Cancel</button>'
                    }
                  html+='         </div>'
                    +'      '
                    +'       '
                    +'      <!-- Too Loop? -->';
             
                            index+=1;
                             console.log('sulod');
               }
             $('.comment-reactor').html(html);
             reload_board_stream(data);
        }
        
        // Reloading the card
        reload_card = function(data){
            console.log('reloading card...');
            popped_card_title_link = $('#heading-card-title').attr('action');
            $(".class-details-reactor").empty();
            cards=JSON.parse(data.cards);
            console.log(data.current_user);
            user=data.current_user;
            comments = "";
            if(data.comments){
                comments=JSON.parse(data.comments);
            }
           
            card_id = cards[0].pk;
            card_name = cards[0].fields.name;
            card_description = cards[0].fields.description;
            if (card_description==null){
              card_description="";
            }
            html = ""
            html += ' <div class="modal fade bd-example-modal-lg" id="CardModal" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">'
                  +'<div class="modal-dialog modal-lg">'
                   +'    <div class="modal-content">'
                   +'       <div class="modal-header">'
                    +'      <div class="left-portion-of-header col-lg-9 col-md-9 col-sm-9">'
                   +'         <h3 id="heading-card-title" data-card_id="'+card_id+'" action="'+popped_card_title_link+'" class="modal-title card-class-title"><strong><div class="reload-title">'+card_name+'</div></strong></h3>'
                  +'          <input id="input-card-title" class="form-control card-class-title display-none" value="'+card_name+'"> '

                   +'         <button name="" id="card-button-update-title"class="btn btn-secondary card-button-add-description mt-3 ml-1 display-none float-right">Update</button>'
                   +'        <button name="" id="card-button-cancel-title"class="btn btn-secondary card-button-add-description mt-3 ml-1 display-none float-right">Cancel</button>'
                   + '       </div>'
                   +'      <div class="right-portion-of-header col-lg-3 col-md-3 col-sm-3">'
                   +'         <button type="button" class="close" data-dismiss="modal" aria-label="Close">'
                   +'           <span aria-hidden="true">&times;</span>'
                   +'         </button>'
                   +'       </div>'
                   +'     </div>'
                   +'       <div class="modal-body">'
                   +'          <div class="left-portion-of-header col-lg-9 col-md-9 col-sm-9">'
                   +'               <h5 class="modal-label-desc" id="exampleModalLabel">Card Description</h5>'

                   +'        </div>'
                    +'        <div class="right-portion-of-header col-lg-3 col-md-3 col-sm-3">'
                    +'              <h5 class="modal-label-manage" id="exampleModalLabel">Manage</h5>'
                    +'       </div>'
                    +'         <div class="left-portion-of-modal col-lg-9 col-md-9 col-sm-9">'

                    +'            <textarea readonly id="text-id-description" class="textarea class-description" placeholder="Card Description">'+card_description+'</textarea>'

                     +'           <button name="" id="card-button-add-description"class="btn btn-secondary card-button-add-description mt-1 float-right display-none">Save</button>'
                    +'            <button name="" id="card-button-cancel-description"class="btn btn-secondary card-button-add-description mt-1 float-right display-none">Cancel</button>'
                    +'          </div>'

                     +'         <div class="right-portion-of-modal col-lg-3 col-md-3 col-sm-3">'
                     +'             <button data-toggle="modal" data-target="#CardMemberModal" id="pop-assign-members" class="btn btn-secondary card-button-invite mt-1" data-dismiss="modal">Members</button>'
                     +'             <button data-toggle="modal" data-target="#DueDateModal" id="pop-due-date" name="MessageBoxModalAlert" class="btn btn-secondary card-button-due-date mt-1" data-dismiss="modal">Due Date</button>'
                     +'             <button  data-toggle="modal" data-target="#ArchiveCardConfirmation"  name="MessageBoxModalAlert" class="btn btn-secondary card-button-due-date mt-1" data-dismiss="modal">Archive</button>'

                     +'         </div>'
                      +'        <!-- Bottom Part -->'
                     +'         <div id="hr-after-description"class="left-portion-of-header col-lg-12 col-md-12 col-sm-12">'
                     +'           <hr class="hr">'
                     +'       </div>'
                     +'       <div class="left-portion-of-header col-lg-9 col-md-9 col-sm-9">'
                     +'             <h5 class="modal-card-add-comment" id="exampleModalLabel">コメントを追加する</h5>'
                     +'             <textarea id="text-comment-area" class="textarea" placeholder="Write a comment"></textarea>'
                      +'            <button id="card-button-add-comment" name="" class="btn btn-secondary card-button-add-comment mt-1 float-right display-none">Save</button>'
                     +'              <button id="card-button-cancel-comment" name="" class="btn btn-secondary card-button-add-comment mt-1 float-right display-none">Cancel</button>'

                     +'      </div>'
                     +'<div class="comment-reactor"> ';
                     if(comments){
                            html += '     <!-- Comments -->'
                         +'      <div class="left-portion-of-header col-lg-12 col-md-12 col-sm-12">'
                         +'           <hr class="hr">'
                         +'       </div>'
                          +'      <div class="left-portion-of-header col-lg-9 col-md-9 col-sm-9">'
                          +'            <h5 class="modal-card-add-comment" id="exampleModalLabel">Comments</h5>'
                          +'     </div>';
                     }
                    
                      index = 0;
                      while(index < comments.length){
                            date_commented = new Date(comments[index].fields.date_commented);
                            date_commented = formatDate(date_commented);
                            html +='      <!-- To Loop -->'
                            +'       <div class="left-portion-of-header col-lg-12 col-md-12 col-sm-12">'
                            +'            <hr class="hr">'
                             +'       </div>'
                             +'         <div class="left-portion-of-header col-lg-9 col-md-9 col-sm-9">'

                             +'             <p class="card-comment-user" id="exampleModalLabel"><strong>'+comments[index].fields.user+'</strong> ('+date_commented+')</p>'
                             +'             '
                             +'             <div  id="DivisionComment-'+comments[index].pk+'" class="card-comments" name="" novalidate="">'+comments[index].fields.comment+'</div>'
                             +'             <textarea id="InputComment-'+comments[index].pk+'" class="textarea card-comments display-none class-input-comment">'+comments[index].fields.comment+'</textarea>';

                             if(user.current_user==comments[index].fields.user){
                                 html+='  <!--  <button data-value="'+comments[index].pk+'" id="EditComment-'+comments[index].pk+'" class="ClassEditComment float-left additional-option-comment link-style btn btn-warning">Edit</button> -->'
                                +'             <button data-value="'+comments[index].pk+'" data-toggle="modal" data-target="#DeleteCommentModal" id="DeleteComment-'+comments[index].pk+'" class="class-delete-comment float-left additional-option-comment link-style btn btn-danger" data-dismiss="modal">Delete</button>'
                                +'           <button data-value="'+comments[index].pk+'" name="" id="card-save-button-'+comments[index].pk+'" class="btn btn-secondary card-button-add-comment mt-1 float-right display-none">Save</button>'
                                +'           <button data-value="'+comments[index].pk+'" name="" id="card-cancel-button-'+comments[index].pk+'" class="class-card-cancel-button btn btn-secondary card-button-add-comment mr-2 mt-1 float-right display-none">Cancel</button>'
                             }
                             html+='         </div>'
                             +'      '
                             +'       '
                              +'      <!-- Too Loop? -->';
             
                            index+=1;
                      }
                      html+=' </div>'
                            +'    </div>'
                            +'  </div>'
                            +'  </div>';
             $(".class-details-reactor").html(html);
             $("#CardModal").modal('show');
             reload_board_stream(data);
        }

        // Reloading the board
        reload_inner_wrapper = function(data){
            columns = JSON.parse(data.column);
            cards = JSON.parse(data.card);
            add_popped_url=$('#list-form').data('url');
            archived_popped_url = $('#hidden-column-archive-values').val();
            update_popped_url = $('#hidden-column-update-values').val();
            add_card_popped_url = $('#hidden-card-add-values').val();
            transfer_popped_url = $("#hidden-transfer-cards").data("url");
            console.log(transfer_popped_url);
            $('.inner-wrap').empty();
            var a = 0;
            html = "";            
            while(a < columns.length){
                column_id = columns[a].pk;
                column_name = columns[a].fields.name

                // リストのHTMLを加える
                html += '<div class="floatbox list-box" data-value="'+column_id+'" data-url="'+transfer_popped_url+'">  ' 
                         + '<div id="existing-label-'+column_id+'"' 
                       +' class= "existing-reactor board_column_header fb" data-value="' + column_id + '"> '
                       + ' <label data-value="'+column_id+'" '
                        + 'class="existing-label form-control title-column-class'
                        + ' board_column_title" placeholder="Add List">'
                        + ' '+column_name+'</label> '
                       +'<form id="archive-form" action="'+archived_popped_url+'"'
                       +' data-url="'+archived_popped_url+'" data-value="'+column_id+'" novalidate="">'
                        +'<a id="archived-settings"  class="list-settings">'
                        +'<button class="link-style list-settings" type="submit">[X]</button></a>'
                        +'</form>'
                         + ' </div> '
                         + '   <form  id="existing-form-'+column_id+'" ' 
                         + '   class="existing-form" action='
                         + '   "'+update_popped_url+'" data-url="' +update_popped_url+'"'
                          + '  data-value="'+column_id+'"> '
                           + '     <input id="exist-list-'+column_id+'" class="form-control '
                           + '      title-column-class" data-value="'+column_id+'"'
                           + '      value="'+column_name+'">'
                           + '     <button name="AddColumn" type="submit" '
                           + '     class="btn btn-success btn-add-list">Update'
                           + '     </button> '
                            + '    <button id="close-add-list" type="button" '
                           + '      class="btn btn-secondary close-add-list"> '
                           + '      Cancel</button>  '
                          + '  </form>'
                          + '<div class="group-cards">';
                             b = 0;
                             while(b < cards.length){
                                if (cards[b].fields.column == columns[a].pk){
                                    html+= ' '
                                        + '<div id="existing-card-'+column_id+'" data-card_id='+cards[b].pk+' class="card-reactor" data-value="'+column_id+'">'
                                        +' <p>'
                                        +' <label data-value="'+column_id+'" class="card-column-class non-editable-add-card">'+cards[b].fields.name+'</label>'
                                        +' </p>'
                                        +'  <form id="archive-form" action="'+archived_popped_url+'" data-url="'+archived_popped_url+'" data-value="'+column_id+'" novalidate="">'
                                        +'  </form>'
                                        +' </div>';
                                }
                                b+=1;
                             }
                              html += '  ' 
                                      + '<!-- Add Card -->'
                                      + '         <form  id="existing-form-'+column_id+'"'
                                      + ' class="existing-form"  data-value="'+column_id+'"'
                                      + ' action=""'
                                      + ' data-url="">'
                                      + ' <input id="exist-list-'+column_id+'"'
                                      + ' class="form-control title-column-class"'
                                      + 'data-value="'+column_id+'" value="'+column_id+'"> '
                                      + ' <button name="AddColumn" type="submit"'
                                      + 'class="btn btn-success btn-add-list">Update</button>' 
                                      + '<button id="close-add-list" type="button" class="btn'
                                      + 'btn-secondary close-add-list">Cancel</button>'  
                                      + '         </form>'
                                      + '</div>'
                                      +'<div class="add-card-division">'
                                      + '       <div class="add-card-reactor-'+column_id+'">'
                                      + '         <label class="form-control title-card-class'
                                      +' editable-add-card" data-value="'+column_id+'"'
                                      +' placeholder="Add List">カードを追加</label>'
                                      + '     </div>'
                                      + '     <form id="card-add-form-column-'+column_id+'"'
                                      + 'class="card-add-form-class toggle-card"'
                                      + 'action="'+add_card_popped_url+'"'
                                      + 'data-url="'+add_card_popped_url+'"' 
                                      + 'data-value="'+column_id+'">'
                                      + '         <input id="add-card-'+column_id+'"' 
                                      + 'class="form-control title-column-class" '
                                      +' placeholder="タイトルを入力してEnter"> '
                                      +'<div class="fb card_add_btns btns_2">'
                                      + '<button id="close-add-card" data-value="'+column_id+'"'
                                      + 'type="button" class="btn btn-secondary close-add-card">'
                                      + 'キャンセル</button>'
                                      + ' <button name="AddColumn" type="submit"'
                                      + 'class="btn btn-success btn-add-card">カードを追加</button>'
                                      +'</div>'
                                      + '     </form>'
                                      +'</div>'
                                      + ' </div>';
                               html+=' </div>';
                a+=1;
            }



            html += '<div class="floatbox list-box add_list_box">'
                  +'<div class="add-input-reactor">'
                      +'<label class="form-control title-column-class board_column_title" placeholder="Add List">リストを追加</label>'
                  +'</div>'
                  +'<form id="list-form" action="'+add_popped_url+'" data-url="'+add_popped_url+'">'
                      +'<input id="add-list" class="form-control title-column-class" placeholder="タイトルを入力してEnter"> '
                      +'<div class="fb list_add_btns btns_2">'
                      +'<button id="close-add-list" type="button" class="btn btn-secondary close-add-list">キャンセル</button>'
                      +'<button name="AddColumn" type="submit" class="btn btn-success btn-add-list">リストを追加</button> '
                      +'</div>'
                  +'</form>'
              +'</div>';
            $('.inner-wrap').html(html);

            init_drag_and_drop_mechanics();
            reload_board_stream(data);
        }
        
});