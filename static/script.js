document.getElementById('predict-btn').addEventListener('click', function() {
    var form = document.getElementById('prediction-form');
    var formData = new FormData(form);
    
    // Convert form data to JSON
    var jsonData = {};
    formData.forEach(function(value, key) {
        jsonData[key] = value;
    });
    
    // Send JSON data to backend for prediction
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => response.json())
    .then(data => {
        // Display prediction result
        var resultDiv = document.getElementById('result');
        if (data.placed == true) {
            resultDiv.innerText = 'Placed';
            resultDiv.innerHTML += "<br>" + "Probability of Placement: " + (data.probability * 100).toFixed(2) + "%";
        } else {
            resultDiv.innerText = 'Not Placed';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
