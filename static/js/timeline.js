
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

// 未完了のアイテム

function scrollToTargetAdjusted( height )
{
    let unDoneChecks = document.querySelectorAll( ".undone .taskCheck" );
    var headerOffset = height;
    var elementPosition = unDoneChecks[ 0 ].getBoundingClientRect().top;
    var offsetPosition = elementPosition + window.pageYOffset - headerOffset;

    window.scrollTo( {
        top: offsetPosition,
        behavior: "smooth"
    } );
}


$windowWidth = window.innerWidth;

$breakPointA = 768;
$breakPointB = 1024;

isMobileSize = ( $windowWidth < $breakPointA );
isTabletSize = ( $windowWidth <= $breakPointB ) && ( $windowWidth > $breakPointA );
isPcSize = ( $windowWidth > $breakPointB );

if ( isMobileSize ) {
    //横幅768px以下（スマホ）に適用させるJavaScriptを記述
    scrollToTargetAdjusted(130);
}

if ( isTabletSize ) {
    //横幅768px以上、1024px以下（タブレット）に適用させるJavaScriptを記述
    scrollToTargetAdjusted( 160 );
}

if ( isPcSize ) {
    //横幅1024px以上（PC）に適用させるJavaScriptを記述
    scrollToTargetAdjusted( 160 );
}


window.onload = function () {
    if ( isMobileSize ) {
        //横幅768px以下（スマホ）に適用させるJavaScriptを記述
        scrollToTargetAdjusted( 130 );
    }

    if ( isTabletSize ) {
        //横幅768px以上、1024px以下（タブレット）に適用させるJavaScriptを記述
        scrollToTargetAdjusted( 160 );
    }

    if ( isPcSize ) {
        //横幅1024px以上（PC）に適用させるJavaScriptを記述
        scrollToTargetAdjusted( 160 );
    }

}





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
                    checkbox.closest( ".unit" ).classList.remove( "undone" );
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
                    checkbox.closest( ".unit" ).classList.add( "undone" );
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


const moveBtn = document.getElementById( "moveBtn" );
moveBtn.addEventListener( 'click', function () {
    
    if ( isMobileSize ) {
        //横幅768px以下（スマホ）に適用させるJavaScriptを記述
        scrollToTargetAdjusted( 130 );
    }

    if ( isTabletSize ) {
        //横幅768px以上、1024px以下（タブレット）に適用させるJavaScriptを記述
        scrollToTargetAdjusted( 160 );
    }

    if ( isPcSize ) {
        //横幅1024px以上（PC）に適用させるJavaScriptを記述
        scrollToTargetAdjusted( 160 );
    }
} );
