


const csrf = Cookies.get( 'csrftoken' );

const checks = document.querySelectorAll( ".taskCheck" );
const createBtn = document.querySelectorAll( ".create-calendar-task" );
const show_task = document.querySelectorAll( "#show_task" );

// タイムラインAJAX
document.addEventListener( "DOMContentLoaded", () => {
    
    // AJAXでカレンダーのタスクを作成する
    const createNote = e =>
    {
        if(e.target !== document.querySelector("#new-list-btn") && !passCreateNote){
            let element = document.createElement('div');
            element.classList.add('form-group');
            element.classList.add('float-left');
            element.innerHTML = `<div class="create-note-box">
            <input type="text" class="input-animate input-note-title" placeholder="Title">
            <textarea class="input-note-text textarea-auto-adjust" placeholder="Take a note..."></textarea>
            <div class="input-color-option">
                <img src = "/static/Icon/paint.png" class="create-note-option" title="Change color">
                <div class="select-color theme-adjust">
                    <span class="select-color-text">Color</span>
                    <input type="color" value = "#202124" id="select-color-input"></input>
                </div>
            </div>
            <img src = "/static/Icon/todo.png" class="create-note-option" title = "Show checkboxes" id="show-checkbox">
            </div>`;
            document.querySelector(".create-note-preview").replaceWith(element);
            document.querySelectorAll(".textarea-auto-adjust").forEach(textarea => {
                textarea.addEventListener("input", () => {
                    textarea.style.height = "5px";
                    textarea.style.height = textarea.scrollHeight + 'px';
                })
            })
            trackUpdateColorInput();
            element.querySelector("#show-checkbox").addEventListener("click", showCheckbox)
            const submitNote = event => {
                if ( !element.contains( event.target ) && document.body.contains( event.target ) || event.target.className === "form-group float-left" )
                {
                    
                    // title変数に、「input-note-title」クラスの値を代入する
                    let title = document.querySelector( ".input-note-title" ).value;
                    let date = document.querySelector( ".input-note-date" ).value;
                    if(title.length){
                        fetch( '/create_task_calendar', {
                            method: "POST",
                            headers: {'X-CSRFToken': csrf},
                            body: JSON.stringify({
                                title: title,
                                date: date
                            })
                        })
                        .then(response => response.json())
                        .then(result =>{
                            if(result["message"] === "Success"){
                                let noteElement = document.createElement('div');
                                document.querySelector(".notes-grid")? noteElement.setAttribute('class', 'note-box m-2'): noteElement.setAttribute("class", "list-note-box")
                                noteElement.setAttribute("draggable", 'true');
                                noteElement.dataset.pk = result["pk"];
                                noteElement.id = `note-${result["pk"]}`;
                                noteElement.style.backgroundColor = color;
                                let tasks = "";
                                if(result["tasks"]){
                                    JSON.parse(result["tasks"]).forEach(task => {
                                        tasks += `<div>
                                            <input type="checkbox" name="${task.pk}" id="task-${task.pk}" class="task" data-pk="${task.pk}">
                                            <label for="task-${task.pk}">${task.fields.todo}</label>
                                        </div>`
                                    })
                                }
                                noteElement.innerHTML = `<div class="box">
                                <h5 class="note-box-title">${title}</h5>
                                ${ note.length ?`
                                <p class="note-box-text">${note}</p>`:`
                                ${tasks}
                                `}
                                <div class="note-option">
                                    <img src="/static/Icon/trash.png" alt="Delete note" id="delete-note-btn" data-pk="${result["pk"]}" title="Delete">
                                    ${note.length?
                                        `<img src="/static/Icon/todo.png" alt = "Show checkbox" id="show-checkbox-note-btn" data-pk="${result["pk"]}" title="Show Checkbox">`
                                        :`<img src="/static/Icon/todo.png" alt = "Hide checkbox" id="hide-checkbox-note-btn" data-pk="${result["pk"]}" title="Hide Checkbox">`
                                    }
                                    <img src="/static/Icon/archive.png" alt="Archive" id="archive-note-btn" data-pk="${result["pk"]}" title="Archive">
                                </div>
                                </div>`;
                                showCheckboxEventListener(noteElement.querySelectorAll("#show-checkbox-note-btn"))
                                hideCheckboxEventListener(noteElement.querySelectorAll("#hide-checkbox-note-btn"))
                                archiveNoteEventListener(noteElement.querySelectorAll("#archive-note-btn"))
                                taskEventListener(noteElement.querySelectorAll(".task"))
                                if(document.querySelector(".notes-grid"))document.querySelector(".notes-grid").insertBefore(noteElement, document.querySelector(".notes-grid").firstChild)
                                else document.querySelector(".notes").insertBefore(noteElement, document.querySelector(".notes").firstChild)
                                editNoteModalEventListener([noteElement])
                                noteElement.querySelector("#delete-note-btn").addEventListener("click", () => {
                                    fetch('/delete_note', {
                                        method: "POST",
                                        headers: {'X-CSRFToken': csrf},
                                        body: JSON.stringify({
                                            "pk": result["pk"]
                                        })
                                    })
                                    .then(response => response.json())
                                    .then(result => {
                                        if(result["message"] === "Success"){
                                            noteElement.parentNode.removeChild(noteElement)
                                        }
                                    })
                                })
                            }
                        })
                    }
                    let newElement = document.createElement("div");
                    newElement.classList.add("form-group")
                    newElement.classList.add("create-note-preview")
                    newElement.classList.add("float-left")
                    newElement.innerHTML = `<div class="create-note-box"><input type="text" class="create-note-input" placeholder="Take a note..."><img src="/static/Icon/todo.png" alt="New list icon" title="New list" id="new-list-btn"></div>`;
                    element.replaceWith(newElement)
                    addNewListEvent()
                    document.body.removeEventListener("click", submitNote)
                    newElement.addEventListener('click', createNote)
                }
            }
            document.body.addEventListener( "click", submitNote )
            
            // 入力するタイトルにフォーカスする
            document.querySelector(".input-note-title").focus()
            return;
        }
        passCreateNote = false
    }

    // カレンダーのタスクを作成する
    const taskCreateListener = checkboxes => {
        checkboxes.forEach( checkbox =>
        {
            // 作成ボタンがクリックされた時
            checkbox.addEventListener( "click", function ()
            {
                
                alert( "aaawww" );
            } )
        } )
    }
    taskCreateListener( createBtn );

    const taskEventListener = checkboxes => {
        checkboxes.forEach( checkbox => {
            checkbox.addEventListener( "change", function ()
            {
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
    taskEventListener( checks );

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
