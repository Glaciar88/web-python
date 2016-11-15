def application(env, start_response):
    	start_response('200 OK', [('Content-Type','text/plain')])
	outp = env['QUERY_STRING'].replace("&", '\n')
    	return [outp]
