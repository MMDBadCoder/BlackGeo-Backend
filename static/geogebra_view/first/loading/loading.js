$(document).ready(function () {
    setTimeout(function () {
        $("#loading").fadeOut("slow");
    }, 1000);


    document.body.last_width = $('#body').width();
    document.body.last_heigth = $('#body').height();

    $(window).on("resize", function () {
        setTimeout(function () {
            last_width = document.body.last_width;
            last_heigth = document.body.last_heigth;
            new_width = $('#body').width();
            new_height = $('#body').height();
            diff = Math.abs(new_width - last_width) + Math.abs(new_height - last_heigth);
            if (diff > 500) {
                location.reload();
            }
        }, 0);
    });

});
