function getWeather() {
    let city = document.getElementById("cityInput").value;
    if (!city) {
        alert("Please enter a city name!");
        return;
    }

    fetch(`http://127.0.0.1:5000/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("weatherResult").innerHTML = `<p>${data.error}</p>`;
            } else {
                document.getElementById("weatherResult").innerHTML = `
                    <h2>${data.city}</h2>
                    <p>Temperature: ${data.temperature}°C</p>
                    <p>Weather: ${data.description}</p>
                    <p>Humidity: ${data.humidity}%</p>
                    <p>Wind Speed: ${data.wind_speed} m/s</p>
                `;
            }
        })
        .catch(error => console.error("Error fetching weather data:", error));
}
