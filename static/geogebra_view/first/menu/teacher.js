$(document).ready(function() {
  function show_question() {
    let card = $("#question-card");
    card.show();
    card.animate({ left: "5px", top: "5px" });
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
  red_item.click(async function() {
    const { value: file } = await Swal.fire({
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
  purple_item.click(function() {
    let names = window.geogebra_api.getAllObjectNames();
    let options = [];
    names.forEach(function(name, index) {
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
      const { value: formValues } = await Swal.fire({
        title: "Pick goals elements",
        width: "80%",
        showCancelButton: false,
        showConfirmButton: false,
        html: '<span class="multi-select-custom"></span>',
        onOpen: function() {
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
        preConfirm: () => {}
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
  orange_item.click(async function() {
    const { value: formValues } = await Swal.fire({
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

  options.forEach(function(option, index) {
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
  lightblue_item.click(async function() {
    const { value: formValues } = await Swal.fire({
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
        options.forEach(function(option, index) {
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

// geogebra_api functions
//
//
//
//
//
//
//
//
//
//
//
//
//
//

let api = window.geogebra_api

api.goalObjects = [];

api.normalColor = function() {
  let names = api.getAllObjectNames();
  names.forEach(function(name, index) {
    api.setColor(name, 52, 100, 251);
  });
};
api.normalColor();

api.setGoalObjects = function(goals) {
  api.goalObjects = goals;
  api.normalColor();
  goals.forEach(function(name, index) {
    api.setColor(name, 255, 0, 10);
    api.setVisible(name, true);
  });
};

api.getGoalObjects = function() {
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

api.registerRemoveListener(removeListener);
api.registerAddListener(addListener);
api.registerRenameListener(renameListener);
