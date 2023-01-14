const csrf = Cookies.get( 'csrftoken' );

var taskCheck = document.querySelectorAll( ".taskCheck" );
var trash = document.querySelectorAll( ".trash-box" );
const createBtn = document.querySelectorAll( ".create-calendar-task" );
const show_task = document.querySelectorAll( "#show_task" );

// タイムラインAJAX
document.addEventListener( "DOMContentLoaded", () => {

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
                                TaskElement.innerHTML = `<p>
                                <label class = "ECM_CheckboxInput"><input type="checkbox" class="taskCheck ECM_CheckboxInput-Input" data-pk="${result["pk"]}"><span class="ECM_CheckboxInput-DummyInput"></span><span class="ECM_CheckboxInput-LabelText"><span class="modal-open task" data-modal-open="modal-task-update">${title}</span></span><div class="meta-box"><div class="trash-box" data-pk="${result["pk"]}"><span class="material-symbols-outlined">delete</span></div></div></label>
                                </p>`;
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

    // タスクを削除する


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