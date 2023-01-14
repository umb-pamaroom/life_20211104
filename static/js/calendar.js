


const csrf = Cookies.get( 'csrftoken' );

const checks = document.querySelectorAll( ".taskCheck" );
const show_task = document.querySelectorAll( "#show_task" );

// タイムラインAJAX
document.addEventListener( "DOMContentLoaded", () => {
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
