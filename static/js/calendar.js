const csrf = Cookies.get( 'csrftoken' );

var taskCheck = document.querySelectorAll( ".taskCheck" );
var trash = document.querySelectorAll( ".trash-box" );
const createBtn = document.querySelectorAll( ".create-calendar-task" );
const show_task = document.querySelectorAll( "#show_task" );

// タイムラインAJAX
document.addEventListener( "DOMContentLoaded", () => {

    // タスクの数を表示する
    // const TaskNumEventListener = boxes => {
    //     boxes.forEach( box =>
    //     {
    //         // 全てのタスク
    //         let taskNum = box.querySelectorAll( ".task-box" );
    //         let taskOkNum = box.querySelectorAll( ".task-box.ok" );

    //         let AllTaskCalendarNum = box.querySelector( ".AllTaskCalendarNum" )
    //         let DoneAllTaskCalendarNum = box.querySelector( ".DoneAllTaskCalendarNum" );
    //         let PercentTask = box.querySelector( ".PercentTask" );
    //         let per = Math.round(taskOkNum.length / taskNum.length * 100);
    //         if ( taskNum.length == 0 ) { per = 100; }

    //         AllTaskCalendarNum.innerHTML = taskNum.length;
    //         DoneAllTaskCalendarNum.innerHTML = taskOkNum.length;
    //         PercentTask.innerHTML = per;
    //     } )
    // }
    // TaskNumEventListener( document.querySelectorAll( ".date-in" ) )

    // タスクを更新する（タスクのタイトルをクリックした時発動）
    const editTaskModalEventListener = boxes => {
        boxes.forEach( box => {
            box.addEventListener( "click", () =>
            {
                // 更新用のモーダルを表示させる
                let editNoteModal = document.querySelector( "#edit-note" );
                editNoteModal.classList.add( "is-open" );

                // 更新するデータをフォームに入力させる
                editNoteModal.querySelector( "#edit-note-title" ).value = box.querySelector( ".note-box-title" ).innerText;
                editNoteModal.querySelector( "#edit-note-title" ).setAttribute( "data-tasktitle", box.dataset.pk );

                editNoteModal.querySelector( "#edit-note-date" ).value = box.getAttribute( "data-date" );
                editNoteModal.querySelector( "#edit-note-date" ).setAttribute( "data-taskdate", box.dataset.pk );

                editNoteModal.querySelector( "#edit-note-des" ).value = box.getAttribute( "data-des" );
                editNoteModal.querySelector( "#edit-note-des" ).setAttribute( "data-taskdes", box.dataset.pk );


                const editTitleEventListener = e =>
                {
                    if ( editNoteModal.querySelector( "#edit-note-title" ).dataset.tasktitle == box.dataset.pk )
                    {
                        fetch( '/update_task_title', {
                            method: "POST",
                            headers: {
                                'X-CSRFToken': csrf
                            },
                            body: JSON.stringify( {
                                "pk": box.dataset.pk,
                                "title": e.target.value
                            } )
                        } )
                            .then( response => response.json() )
                            .then( result =>
                            {
                                if ( result["message"] === "Success" )
                                {
                                    box.querySelector( ".note-box-title" ).innerText = e.target.value;
                                }
                            } )
                    }
                }
                editNoteModal.querySelector( "#edit-note-title" ).addEventListener( "input", editTitleEventListener );

                const editNoteEventListener = e =>
                {
                    if ( editNoteModal.querySelector( "#edit-note-date" ).dataset.taskdate == box.dataset.pk )
                    {
                        fetch( '/update_task_text', {
                            method: "POST",
                            headers: {
                                'X-CSRFToken': csrf
                            },
                            body: JSON.stringify( {
                                "pk": box.dataset.pk,
                                "description": e.target.value
                            } )
                        } )
                            .then( response => response.json() )
                            .then( result =>
                            {
                                if ( result["message"] === "Success" )
                                {
                                    box.setAttribute( "data-des", e.target.value );
                                }
                                if ( e.target.value == "" )
                                {
                                    box.closest( ".task-box" ).classList.remove( "des" );
                                } else
                                {
                                    box.closest( ".task-box" ).classList.add( "des" );
                                }
                            } )
                    }
                }
                editNoteModal.querySelector( "#edit-note-des" ).addEventListener( "input", editNoteEventListener );


                const editDateEventListener = e =>
                {
                    if ( editNoteModal.querySelector( "#edit-note-des" ).dataset.taskdes == box.dataset.pk )
                    {
                        fetch( '/update_task_date', {
                            method: "POST",
                            headers: {
                                'X-CSRFToken': csrf
                            },
                            body: JSON.stringify( {
                                "pk": box.dataset.pk,
                                "date": e.target.value
                            } )
                        } )
                            .then( response => response.json() )
                            .then( result =>
                            {
                                if ( result["message"] === "Success" )
                                {
                                    box.setAttribute( "data-date", e.target.value );
                                    location.reload();
                                }
                            } )
                    }
                }
                editNoteModal.querySelector( "#edit-note-date" ).addEventListener( "input", editDateEventListener );

            } )
        } )
    }
    editTaskModalEventListener( document.querySelectorAll( ".ECM_CheckboxInput-LabelText" ) )

    // カレンダーのタスクを作成する
    const taskCreateListener = checkboxes => {
        checkboxes.forEach( checkbox => {
            // 作成ボタンがクリックされた時
            checkbox.addEventListener( "click", function () {
                // 値の取得
                let title = checkbox.closest( ".modal-content" ).firstElementChild.firstElementChild.value;
                let date = checkbox.closest( ".modal-content" ).firstElementChild.lastElementChild.value;
                let td = checkbox.closest( "td" );
                let modal_calendar = checkbox.closest( ".modal" );
                let text_calendar = modal_calendar.lastElementChild.firstElementChild.firstElementChild.firstElementChild;
                let dateTask = td.firstElementChild.firstElementChild.lastElementChild;

                // サーバにデータを送る
                if ( title.length ) {
                    fetch( '/create_task_calendar', {
                            method: "POST",
                            headers: {
                                'X-CSRFToken': csrf
                            },
                            body: JSON.stringify( {
                                title: title,
                                date: date
                            } )
                        } )
                        .then( response => response.json() )
                        .then( result => {
                            // 無事タスクをサーバで作成できたら
                            if ( result[ "message" ] === "Success" ) {
                                // タスクの要素を作成する
                                let TaskElement = document.createElement( 'div' );
                                TaskElement.classList.add( "task-box" );
                                TaskElement.id = `task-box-${result["pk"]}`;
                                TaskElement.innerHTML = `<p><span class="ECM_CheckboxInput"><label><input type="checkbox" class="taskCheck ECM_CheckboxInput-Input" data-pk="${result["pk"]}" {% if task.complete %}checked{% endif %}><span class="ECM_CheckboxInput-DummyInput"></span></label><span class="ECM_CheckboxInput-LabelText" data-pk="${result["pk"]}" data-date="{{day.year}}-{% if day.month < 10 %}0{% endif %}{{day.month}}-{% if day.day < 10 %}0{% endif %}{{day.day}}" data-des="{{task.description}}"><span class="task note-box-title" data-pk="${result["pk"]}">${title}</span></span></span><div class="meta-box"><div class="trash-box" data-pk="${result["pk"]}"><span class="material-symbols-outlined">delete</span></div></div></p>`;
                                dateTask.appendChild( TaskElement );
                                var taskCheck = document.querySelectorAll( ".taskCheck" );
                                taskEventListener();
                                var trash = document.querySelectorAll( ".trash-box" );
                                trashListener();
                                modal_calendar.classList.remove( "is-open" );
                                // alert(title);
                                // title = "";
                                // alert( title );
                            }
                        } )

                }
            } )
        } )
    }
    taskCreateListener( createBtn );

    // タスクを削除する
    const trashListener = checkboxes => {
        var trash = document.querySelectorAll( ".trash-box" );
        trash.forEach( btn => {
            btn.addEventListener( "click", () => {
                fetch( '/delete_task_calendar', {
                        method: "POST",
                        headers: {
                            'X-CSRFToken': csrf
                        },
                        body: JSON.stringify( {
                            "pk": btn.dataset.pk
                        } )
                    } )
                    .then( response => response.json() )
                    .then( result => {
                        if ( result[ "message" ] === "Success" ) {
                            let noteElement = document.querySelector( `#task-box-${btn.dataset.pk}` );
                            noteElement.parentNode.removeChild( noteElement );
                        }
                    } )
            } )
        } )
    }
    trashListener();



    const taskEventListener = checkboxes => {
        var taskCheck = document.querySelectorAll( ".taskCheck" );
        taskCheck.forEach( checkbox => {
            checkbox.addEventListener( "change", function () {
                if ( this.checked ) {
                    fetch( '/check_task_calendar', {
                        method: "POST",
                        headers: {
                            'X-CSRFToken': csrf
                        },
                        body: JSON.stringify( {
                            "pk": checkbox.dataset.pk
                        } )
                    } )
                    // 祖先要素を取得
                    checkbox.closest( ".task-box" ).classList.add( "ok" );
                } else {
                    fetch( '/uncheck_task_calendar', {
                        method: "POST",
                        headers: {
                            'X-CSRFToken': csrf
                        },
                        body: JSON.stringify( {
                            "pk": checkbox.dataset.pk
                        } )
                    } )
                    checkbox.closest( ".task-box" ).classList.remove( "ok" );
                }
            } )
        } )
    }
    taskEventListener();



    const show_task_listener = checkboxes => {
        checkboxes.forEach( checkbox => {
            checkbox.addEventListener( "change", function () {
                if ( this.checked ) {
                    fetch( '/show_task_calendar', {
                        method: "POST",
                        headers: {
                            'X-CSRFToken': csrf
                        },
                        body: JSON.stringify( {
                            "pk": checkbox.dataset.pk
                        } )
                    } )
                    checkbox.closest( ".page-container" ).classList.add( "done_task_calendar_show" );
                } else {
                    fetch( '/unshow_task_calendar', {
                        method: "POST",
                        headers: {
                            'X-CSRFToken': csrf
                        },
                        body: JSON.stringify( {
                            "pk": checkbox.dataset.pk
                        } )
                    } )
                    checkbox.closest( ".page-container" ).classList.remove( "done_task_calendar_show" );
                }
            } )
        } )
    }
    show_task_listener( show_task );
} )