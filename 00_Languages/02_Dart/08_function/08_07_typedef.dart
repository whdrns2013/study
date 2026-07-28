




Map<String, String> getIdPasswd(String username){

  Map<String, Map<String, String>> userData;
  Map<String, String> kim = {"imsuperman" : "passwd1234"};
  Map<String, String> lee = {"lovelovelove" : "fjnsdfuqb"};
  Map<String, String> park = {"dkdlelanjffhgo" : "qlalfqjsgh"};

  userData = {"kim" : kim, "lee" : lee, "park" : park};
  Map<String, String>? result = userData[username];
  result ??= {'fail' : 'no data'};

  return result;
}


typedef userInfo = Map<String, String>;

userInfo getIdPasswd2(String username){

  Map<String, userInfo> userData;
  userInfo kim = {"imsuperman" : "passwd1234"};
  userInfo lee = {"lovelovelove" : "fjnsdfuqb"};
  userInfo park = {"dkdlelanjffhgo" : "qlalfqjsgh"};

  userData = {"kim" : kim, "lee" : lee, "park" : park};
  userInfo? result = userData[username];
  result ??= {'fail' : 'no data'};

  return result;
}

void main() {
  Map<String, String> result = getIdPasswd('kim');
  print(result);
}