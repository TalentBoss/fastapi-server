def ResponseModel(data, msg):
    return {
      'data': data,
      'code': 200,
      'message': msg
    }


def ErrorResponseModel(err, code, msg):
    return {
      'error': err,
      'code': code,
      'message': msg
    }
