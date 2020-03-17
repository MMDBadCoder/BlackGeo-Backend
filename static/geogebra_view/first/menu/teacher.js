$(document).ready(function () {
    function show_question() {
        let card = $("#question-card");
        card.show();
        card.animate({left: "5px", top: "5px"});
    }

    let icon;

    //green
    let green_item = $(".green-mini-menu");
    icon = $('<i class="window maximize outline large icon"></i>');
    green_item.append(icon);
    green_item.prop("title", "Problem window");
    green_item.click(show_question);

    //blue
    let blue_item = $(".blue-mini-menu");
    icon = $('<i class="eye large icon"></i>');
    blue_item.append(icon);
    blue_item.prop("title", "Problem Page");

    //red
    let red_item = $(".red-mini-menu");
    icon = $('<i class="image large icon"></i>');
    red_item.append(icon);
    red_item.prop("title", "Set problem image");
    red_item.click(async function () {
        const {value: file} = await Swal.fire({
            title: "Select image",
            input: "file",
            inputAttributes: {
                accept: "image/*",
                "aria-label": "Upload your profile picture"
            }
        });

        if (file) {
            const reader = new FileReader();
            reader.onload = e => {
                Swal.fire({
                    title: "Your uploaded picture",
                    imageUrl: e.target.result,
                    imageAlt: "The uploaded picture"
                });
            };
            reader.readAsDataURL(file);
        }
    });

    //purple
    let purple_item = $(".purple-mini-menu");
    icon = $('<i class="check circle large icon"></i>');
    purple_item.append(icon);
    purple_item.prop("title", "Goal elements");
    purple_item.click(function () {
        let names = window.geogebra_api.getAllObjectNames();
        let options = [];
        names.forEach(function (name, index) {
            let definition = window.geogebra_api.getDefinitionString(name);
            if (definition === "") {
                definition = window.geogebra_api.getObjectType(name);
            }
            let option = {
                label: name + " (" + definition + ")",
                value: name
            };
            options.push(option);
        });

        (async () => {
            const {value: formValues} = await Swal.fire({
                title: "Pick goals elements",
                width: "80%",
                showCancelButton: false,
                showConfirmButton: false,
                html: '<span class="multi-select-custom"></span>',
                onOpen: function () {
                    var customIcon = document.createElement("img");
                    customIcon.src = "./menu/select-pure/icon.svg";
                    var customIconMulti = new SelectPure(".multi-select-custom", {
                        options: options,
                        value: window.geogebra_api.getGoalObjects(),
                        multiple: true,
                        inlineIcon: customIcon,
                        autocomplete: true,
                        onChange: value => {
                            console.log(value);
                            window.geogebra_api.setGoalObjects(value);
                        },
                        classNames: {
                            select: "select-pure__select",
                            dropdownShown: "select-pure__select--opened",
                            multiselect: "select-pure__select--multiple",
                            label: "select-pure__label",
                            placeholder: "select-pure__placeholder",
                            dropdown: "select-pure__options",
                            option: "select-pure__option",
                            autocompleteInput: "select-pure__autocomplete",
                            selectedLabel: "select-pure__selected-label",
                            selectedOption: "select-pure__option--selected",
                            placeholderHidden: "select-pure__placeholder--hidden",
                            optionHidden: "select-pure__option--hidden"
                        }
                    });
                },
                focusConfirm: false,
                preConfirm: () => {
                }
            });
            //   if (formValues) {
            //     let text = window.reply_post_editor.html.get();
            //     if (text === "") {
            //       Swal.fire({
            //         icon: "error",
            //         title: "Empty text ...!"
            //       });
            //     } else {
            //       if (inline_editor !== undefined) {
            //         inline_editor.html.set(text);
            //       }
            //       func(text);
            //     }
            //   }
        })();
    });

    //orange
    let orange_item = $(".orange-mini-menu");
    icon = $('<i class="align justify large icon"></i>');
    orange_item.append(icon);
    orange_item.prop("title", "Problem content and title");
    orange_item.click(async function () {
        const {value: formValues} = await Swal.fire({
            title: "Fill the blanks",
            html:
                '<input placeholder="Problem title" id="swal-input1" class="swal2-input">' +
                '<textarea placeholder="Problem content" style="height: 100px" id="swal-input2" class="swal2-input">',
            focusConfirm: false,
            preConfirm: () => {
                return document.getElementById("swal-input1").value;
            }
        });

        if (formValues) {
            Swal.fire(JSON.stringify(formValues));
        }
    });

    //lightblue
    let lightblue_item = $(".lightblue-mini-menu");
    icon = $('<i class="dollar sign large icon"></i>');
    lightblue_item.append(icon);
    lightblue_item.prop("title", "Pricing");

    let form_html =
        "<br>" +
        "<strong style='float: left; font-size: 20px;'>Reaching the goals:</strong>" +
        '<input placeholder="reward of Reaching the goals" id="swal-reward-input" class="swal2-input" type="number" style="max-width: 100%">' +
        "<br>";
    let options = [
        {
            name: "POINT",
            image_url: "https://wiki.geogebra.org/uploads/d/dc/Tool_New_Point.gif",
            value: 0
        },
        {
            name: "JOIN",
            image_url:
                "https://wiki.geogebra.org/uploads/d/d2/Tool_Line_through_Two_Points.gif",
            value: 1
        },
        {
            name: "segment",
            image_url:
                "https://wiki.geogebra.org/uploads/c/cd/Tool_Segment_between_Two_Points.gif",
            value: 1
        },
        {
            name: "CIRCLE_TWO_POINTS",
            image_url:
                "https://wiki.geogebra.org/uploads/1/1e/Tool_Circle_Center_Point.gif",
            value: 1
        },
        {
            name: "COMPASSES",
            image_url: "https://wiki.geogebra.org/uploads/e/e3/Tool_Compasses.gif",
            value: 1
        },
        {
            name: "CIRCLE_THREE_POINTS",
            image_url:
                "https://wiki.geogebra.org/uploads/b/bc/Tool_Circle_3Points.gif",
            value: 5
        },
        {
            name: "LINE_BISECTOR",
            image_url:
                "https://wiki.geogebra.org/uploads/1/10/Tool_Perpendicular_Bisector.gif",
            value: 3
        },
        {
            name: "ORTHOGONAL",
            image_url:
                "https://wiki.geogebra.org/uploads/7/78/Tool_Perpendicular_Line.gif",
            value: 4
        },
        {
            name: "MIDPOINT",
            image_url:
                "https://wiki.geogebra.org/uploads/1/1c/Tool_Midpoint_or_Center.gif",
            value: 3
        },
        {
            name: "PARALLEL",
            image_url:
                "https://wiki.geogebra.org/uploads/f/fc/Tool_Parallel_Line.gif",
            value: 4
        },
        {
            name: "ANGULAR_BISECTOR",
            image_url:
                "https://wiki.geogebra.org/uploads/e/ed/Tool_Angular_Bisector.gif",
            value: 3
        }
    ];

    options.forEach(function (option, index) {
        let item = '<img src="' + option.image_url + '">';
        item +=
            '<input placeholder="cost of each ' +
            option.name +
            '" id="swal-' +
            option.name +
            '-input" value="' +
            option.value +
            '" class="swal2-input" type="number" style="max-width: 100%">';
        form_html += item;
    });
    lightblue_item.click(async function () {
        const {value: formValues} = await Swal.fire({
            title: "Specify the cost of each element",
            html: form_html,
            focusConfirm: false,
            preConfirm: () => {
                let result = [
                    {
                        name: "reward",
                        value: document.getElementById("swal-reward-input").value
                    }
                ];
                options.forEach(function (option, index) {
                    let id = "swal-" + option.name + "-input";
                    let value = document.getElementById(id).value;
                    if (value !== "") {
                        result.push({
                            name: option.name,
                            value: value
                        });
                    }
                });
                return result;
            }
        });

        if (formValues) {
            Swal.fire(JSON.stringify(formValues));
        }
    });
});

//
//
//
//
//
//
//
// geogebra_api functions and init

window.ggbBase64 =
    "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";

function init_geogebra() {
    let container = document.getElementById("ggb-container");
    let ggb_applet = document.createElement("div");
    ggb_applet.id = "ggb-element";
    container.appendChild(ggb_applet);

    let top_navbar_height = $("#top-navbar").height();
    $("#ggb-element").css("padding-top", top_navbar_height);

    let height = $("#ggb-element").height();
    let width = $("#ggb-element").width();

    var parameters = {
        id: "app1",
        prerelease: false,
        width: width,
        height: height,
        showToolBar: true,
        borderColor: "blue",
        showMenuBar: false,
        showAlgebraInput: false,
        showResetIcon: true,
        enableLabelDrags: false,
        enableShiftDragZoom: true,
        enableRightClick: true,
        capturingThreshold: null,
        showToolBarHelp: false,
        errorDialogsActive: true,
        useBrowserForJS: false,
        showLogging: true,
        enableCAS: false,
        errorDialogsActive: false,
        // customToolBar: '1|2',
        ggbBase64: window.ggbBase64
    };

    parameters.appletOnLoad = function (api) {
        api.setGridVisible(false);
        window.geogebra_api = api;
        teacher_features(api);
    };

    window.ggbApp = new GGBApplet(parameters);
    ggbApp.inject("ggb-element");
}

function create_new_geogebra() {
    if (document.readyState === "complete") {
        init_geogebra();
    } else {
        window.addEventListener("load", function () {
            init_geogebra();
        });
    }
}

// $(window).on("resize", function() {
//   $("#ggb-element").remove();
//   create_new_geogebra();
// });

create_new_geogebra();


function teacher_features(api) {

    api.goalObjects = [];

    api.normalColor = function () {
        let names = api.getAllObjectNames();
        names.forEach(function (name, index) {
            api.setColor(name, 52, 100, 251);
        });
    };
    api.normalColor();

    api.setGoalObjects = function (goals) {
        api.goalObjects = goals;
        api.normalColor();
        goals.forEach(function (name, index) {
            api.setColor(name, 255, 0, 10);
            api.setVisible(name, true);
        });
    };

    api.getGoalObjects = function () {
        return api.goalObjects;
    };

    function renameListener(oldObjName, newObjName) {
        if (api.goalObjects.includes(oldObjName)) {
            api.goalObjects = api.goalObjects.filter(i => i !== oldObjName);
            api.goalObjects.push(newObjName);
        }
    }

    function removeListener(objName) {
        if (api.goalObjects.includes(objName)) {
            api.goalObjects = api.goalObjects.filter(i => i !== objName);
        }
    }

    function addListener(objName) {
        api.setColor(objName, 52, 100, 251);
    }

    function clickListener(objName){
        if(api.getMode() !== 0){
            return;
        }
        if(api.goalObjects.includes(objName)){
            removeListener(objName);
        }else {
            api.goalObjects.push(objName);
        }
        api.setGoalObjects(api.goalObjects);
    }

    api.registerClickListener(clickListener);
    api.registerRemoveListener(removeListener);
    api.registerAddListener(addListener);
    api.registerRenameListener(renameListener);
}

