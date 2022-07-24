#ifndef INCLUDE_INFRARE
#define INCLUDE_INFRARE

extern char url[] = "********";
extern char server[] = "********";


typedef struct http_request {
    char header[256];
    char body[64];
}HTTP_REQUEST;

typedef struct indoor_env {
    double temp;
    double hum;
    double press;
}INDOOR_ENV

void WifiConnect();
void MakeRequestHeader(char *header);
void MakeRequestBody(char *body, INDOOR_ENV indoorEnv);
void ParseResponseBody(char *response_body, COMMAND_OPTION *option);
void ParseResponse(COMMAD_OPTION *cmd_option);
void SendRequest(INDDOR_ENV indoorEnv);

#endif
