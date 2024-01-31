function counter() {
   
    // Get the current value of the input field
    var currentValue = parseFloat(document.getElementById("count").value) || 0;

    // Increment the value by 1
    var newValue = currentValue + 1;

    // Update the input field with the new value
    document.getElementById("count").value = newValue;
}

function clear_counter() {
    // Clear the input field
    document.getElementById("count").value = '';
}