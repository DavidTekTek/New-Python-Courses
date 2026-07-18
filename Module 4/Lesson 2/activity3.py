import tkinter as tk
from tkinter import ttk, messagebox
import requests

WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def get_coordinates(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city_name,
        "count": 1,
        "language": "en",
        "format": "json",
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    results = data.get("results")
    if not results:
        return None
    location = results[0]
    return {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "name": location.get("name", city_name),
        "country": location.get("country", ""),
    }


def get_forecast(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min,weathercode",
        "timezone": "auto",
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def format_forecast(data, location_name, country):
    daily = data.get("daily", {})
    dates = daily.get("time", [])
    max_temps = daily.get("temperature_2m_max", [])
    min_temps = daily.get("temperature_2m_min", [])
    codes = daily.get("weathercode", [])

    if not dates:
        return "No forecast data available."

    lines = [f"Weather forecast for {location_name}, {country}".strip(", ")]
    lines.append("".ljust(50, "-"))
    for date, max_temp, min_temp, code in zip(dates, max_temps, min_temps, codes):
        description = WEATHER_CODES.get(code, "Unknown weather")
        lines.append(
            f"{date}: {description}. High: {max_temp}°C, Low: {min_temp}°C"
        )
    return "\n".join(lines)


def show_forecast():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input required", "Enter a city name first.")
        return

    try:
        location = get_coordinates(city)
        if not location:
            messagebox.showerror("Location not found", "Could not find the city. Try a different name.")
            return

        forecast_data = get_forecast(location["latitude"], location["longitude"])
        text = format_forecast(forecast_data, location["name"], location["country"])
        forecast_output.config(state="normal")
        forecast_output.delete("1.0", tk.END)
        forecast_output.insert(tk.END, text)
        forecast_output.config(state="disabled")
    except requests.RequestException:
        messagebox.showerror("Network error", "Unable to retrieve weather data. Check your connection.")
    except Exception as err:
        messagebox.showerror("Error", f"An error occurred: {err}")


root = tk.Tk()
root.title("Weather Forecast")
root.geometry("520x380")
root.resizable(False, False)

main_frame = ttk.Frame(root, padding=16)
main_frame.pack(fill=tk.BOTH, expand=True)

header = ttk.Label(main_frame, text="Weather Forecast", font=("Segoe UI", 18, "bold"))
header.pack(pady=(0, 12))

city_frame = ttk.Frame(main_frame)
city_frame.pack(fill=tk.X, pady=(0, 12))

city_label = ttk.Label(city_frame, text="City:")
city_label.pack(side=tk.LEFT, padx=(0, 8))

city_entry = ttk.Entry(city_frame, width=32)
city_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
city_entry.focus()

search_button = ttk.Button(city_frame, text="Get Forecast", command=show_forecast)
search_button.pack(side=tk.LEFT, padx=(8, 0))

forecast_output = tk.Text(main_frame, height=14, wrap=tk.WORD, state="disabled", padx=8, pady=8)
forecast_output.pack(fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(forecast_output, command=forecast_output.yview)
forecast_output.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()
