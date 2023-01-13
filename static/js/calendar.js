


const csrf = Cookies.get( 'csrftoken' );

const checks = document.querySelectorAll( ".taskCheck" );

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
                let doneChecks = document.querySelectorAll( ".done .taskCheck" );
            } )
        } )
    }
    taskEventListener( document.querySelectorAll( ".taskCheck" ) )
} )
