data = {
    "success": [],
    "wrong": []
};

$("tbody").on("click", "td",
    function () {
        var allCellsInRow = $(this).siblings("td");
        $.each(allCellsInRow, function () {
            $(this).removeClass("bg-success");
            $(this).removeClass("bg-danger");
        });

        $(this).addClass("bg-success");
    });

$("th").on("dblclick", null,
    function () {
        if (this.className === "bg-danger") {
            console.log('wut');
            this.className = " ";
        } else {
            this.className = "bg-danger";
        }
    });

$("button").on("click", null, function () {
    data.success = [];
    data.wrong = [];

    var allRows = $("tbody").children();

    $.each(allRows, function () {

            var cells = $(this).children();


            var header = cells.slice(0, 1);
            var rest = cells.slice(1);

            console.log('wut',header)

            if (header.hasClass("bg-danger")) {

                data.success.push({
                    "oldLink": header.text(),
                    "newLink": 'not found'
                });
                console.log('not found');
            } else if (rest.length === 1) {
                data.success.push({
                    "oldLink": header.text(),
                    "newLink": $(rest[0]).text()
                })
            } else {
                $.each(rest, function () {
                    if ($(this).hasClass("bg-success")) {
                        data.success.push({
                            "oldLink": header.text(),
                            "newLink": $(this).text()
                        })
                    }

                })
            }


        }
    );

    $.ajax({
        type: "POST",
        method: "POST",
        url: "/linker/about/save/",
        data: data
    });
});