
typedef ForecastData = List<Map<String,dynamic>>;

class ForecastDaily {
  String date, weather;
  int temp;
  double hum;

  ForecastDaily.fromJson(Map<String, dynamic> forecastJson)
      : this.date = forecastJson['date'],
        this.weather = forecastJson['weather'],
        this.temp = forecastJson['temp'],
        this.hum = forecastJson['hum'];

  void announceTodaysWeather(){
    print('today is $date. weather is $weather and $temp temp, $hum hum.');
  }
}

void main() {
  // ~ get some Json datas ~ //

  ForecastData forecastData = [
    {'date':'2024-01-21','weather':'fine', 'temp':25, 'hum':0.5},
    {'date':'2024-01-22','weather':'cloud','temp':10,'hum':0.75},
    {'date':'2024-01-23','weather':'rain','temp':15,'hum':0.95},
    {'date':'2024-01-24','weather':'snow','temp':1,'hum':0.9},
  ];

  // make daily class and announce
  forecastData.forEach((forecastJson){
    var forecast = ForecastDaily.fromJson(forecastJson);
    forecast.announceTodaysWeather();
  });

}