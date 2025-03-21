from enum import Enum

class StatusCode(Enum):
    OK                         = 200
    CREATED                    = 201
    ACCEPTED                   = 202
    NO_CONTENT                 = 204
    MOVED_PERMANENTLY          = 301
    BAD_REQUEST                = 400
    UNAUTHORIZED               = 401
    FORBIDDEN                  = 403
    NOT_FOUND                  = 404
    NOT_ALLOWED                = 405
    SERVER_ERROR               = 500
    BAD_GATEWAY                = 502
    SERVICE_UNAVAILABLE        = 503
    HTTP_VERSION_NOT_SUPPORTED = 505

status_code_description = {
    StatusCode.OK                         : "ok",
    StatusCode.CREATED                    : "created",
    StatusCode.ACCEPTED                   : "accepted",
    StatusCode.NO_CONTENT                 : "no_content",
    StatusCode.MOVED_PERMANENTLY          : "moved_permanently",
    StatusCode.BAD_REQUEST                : "bad_request",
    StatusCode.UNAUTHORIZED               : "unauthorized",
    StatusCode.FORBIDDEN                  : "forbidden",
    StatusCode.NOT_FOUND                  : "not_found",
    StatusCode.NOT_ALLOWED                : "not_allowed",
    StatusCode.SERVER_ERROR               : "server_error",
    StatusCode.BAD_GATEWAY                : "bad_gateway",
    StatusCode.SERVICE_UNAVAILABLE        : "service_unavailable",
    StatusCode.HTTP_VERSION_NOT_SUPPORTED : "http_version_not_supported",
}
