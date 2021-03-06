var customIcon = document.createElement("img");
customIcon.src = "./icon.svg";
var customIconMulti = new SelectPure(".multi-select-custom", {
  options: [
    {
      label: "New York",
      value: "NY"
    },
    {
      label: "Washington",
      value: "WA"
    },
    {
      label: "California",
      value: "CA"
    },
    {
      label: "New Jersey",
      value: "NJ"
    },
    {
      label: "North Carolina",
      value: "NC"
    }
  ],
  value: ["NY", "CA"],
  multiple: true,
  inlineIcon: customIcon,
  autocomplete: true,
  onChange: value => {
    console.log(value);
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
