# <process type>: <command>
# https://devcenter.heroku.com/articles/procfile#procfile-format
#
# STEP2
# web: uvicorn training.step2.hello:app
# web: uvicorn training.hello:app
web: uvicorn source.hello:app --host=0.0.0.0 --port=${PORT:-5000}
