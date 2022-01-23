
const csrf = Cookies.get( 'csrftoken' );

// %
const persentNumber = document.getElementById( "persentNumber" );
const checks = document.querySelectorAll( ".taskCheck" );
const ChecksAll = document.getElementById( "ChecksAll" );
const doneChecksSpan = document.getElementById( "doneChecks" );

// タイムラインのアイテムの数
let checksNumbers = checks.length;

// 完了しているタイムラインのアイテムの数
let doneChecks = document.querySelectorAll( ".done .taskCheck" );
let doneChecksNumbers = doneChecks.length;

persentNumber.innerHTML = Math.round( doneChecksNumbers / checksNumbers * 100 );
ChecksAll.innerHTML = checksNumbers;
doneChecksSpan.innerHTML = doneChecksNumbers;

// タイムラインAJAX
document.addEventListener( "DOMContentLoaded", () => {
    const taskEventListener = checkboxes => {
        checkboxes.forEach( checkbox => {
            checkbox.addEventListener( "change", function ()
            {
                if ( this.checked ) {
                    fetch( '/check_task', {
                        method: "POST",
                        headers: {
                            'X-CSRFToken': csrf
                        },
                        body: JSON.stringify( {
                            "pk": checkbox.dataset.pk
                        } )
                    } )
                    // 祖先要素を取得
                    checkbox.closest( ".unit" ).classList.add( "done" );
                } else {
                    fetch( '/uncheck_task', {
                        method: "POST",
                        headers: {
                            'X-CSRFToken': csrf
                        },
                        body: JSON.stringify( {
                            "pk": checkbox.dataset.pk
                        } )
                    } )
                    checkbox.closest( ".unit" ).classList.remove( "done" );
                }
                let doneChecks = document.querySelectorAll( ".done .taskCheck" );
                persentNumber.innerHTML = Math.round( doneChecks.length / checksNumbers * 100 );
                ChecksAll.innerHTML = checksNumbers;
                doneChecksSpan.innerHTML = doneChecks.length;
            } )
        } )
    }
    taskEventListener( document.querySelectorAll( ".taskCheck" ) )
} )

// チェックボックスを全てリセット
const ResetBtn = document.getElementById( "checkBoxReset" );
ResetBtn.addEventListener( 'click', function () {
    
    for ( const check of checks ) {
        check.checked = false;
        check.closest( ".unit" ).classList.remove( "done" );
        fetch( '/uncheck_task', {
            method: "POST",
            headers: {
                'X-CSRFToken': csrf
            },
            body: JSON.stringify( {
                "pk": check.dataset.pk
            } )
        } )
    }
    ResetBtn.closest( ".modal" ).classList.remove( "is-open" );
} );