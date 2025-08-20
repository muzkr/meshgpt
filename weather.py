from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


class WeatherForecast:
    """
    A class to retrieve weather forecasts using the Open-Meteo API.
    The timezone is fixed to UTC+8 (Beijing Time).

    Attributes:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
    """

    def __init__(self):
        """
        Initializes the WeatherForecast instance with location.

        Args:
            latitude (float): Latitude of the location.
            longitude (float): Longitude of the location.
        """

        path = "./model/Phi-3-mini-4k-instruct"
        model = AutoModelForCausalLM.from_pretrained(
            path,
            device_map="cuda",
            torch_dtype="auto",
            trust_remote_code=True,
        )
        tokenizer = AutoTokenizer.from_pretrained(path)
        self.generator = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            return_full_text=False,
            max_new_tokens=16,
            do_sample=False,
        )

    def get_forecast(self, message: str):
        """
        Retrieves the weather forecast for the specified number of hours.

        Args:
            forecast_hours (int): Number of hours to retrieve the forecast for.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing hourly forecast data.

        Raises:
            Exception: If forecast data has not been fetched yet.
            ValueError: If forecast_hours is not a positive integer.
        """

        out = self.generator(
            [{"role": "user", "content": message + ". 请回答不多于20个字"}])
        return out[0]["generated_text"].strip()


def main():
    wc = WeatherForecast()
    fc = wc.get_forecast("tell me a funny story?")
    print(fc)

    fc = wc.get_forecast("什么鬼")
    print(fc)


if __name__ == "__main__":
    main()
