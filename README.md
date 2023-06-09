# solo-viz
Visualization for ckpool solo miners. Visualize your Proof of Work.

My first time using [streamlit](https://docs.streamlit.io/library/get-started/main-concepts).

## How to run locally
  - Clone down code locally
  - Create a virtual environment -> `python -m venv venv`
  - Activate virtual environment -> `source venv/bin/activate`
  - Navigate to app directory -> `cd app`
  - Install dependencies -> `pip install -r requirements.txt`
  - Then run -> `streamlit run solo_stats.py`

## How to run with docker
  - Build Docker container -> `docker build -t streamlit .`
  - Run docker container -> `docker run -p 8501:8501 streamlit`
  - To view your app, browse to http://0.0.0.0:8501 or http://localhost:8501

## For more on the dashboard
  - [Check out my youtube video on it](https://youtu.be/XfvF94boFAM)
  - [Check out my podcast episode](https://spotifyanchor-web.app.link/e/sedaunPYeAb)
  - [Check out my newsletter](https://www.jordanlaster.com/the-world-of-bitcoin-solo-mining/)

## Streamlit Tips and Tricks
- How to modify configuration file -> [.streamlit/config.toml](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)
- To view all available configuration options: `streamlit config show`
- Use [caching](https://docs.streamlit.io/library/advanced-features/caching) for functions that return data (Data is cached here for 5mins)
- [Chart Elements](https://docs.streamlit.io/library/api-reference#chart-elements)

### Deploying Streamlit App
You can use Streamlit Community Cloud to deploy, manage, and share your app for free.

It works in 3 simple steps:

    - Put your app in a public GitHub repo (and make sure it has a requirements.txt!)
    - Sign into [share.streamlit.io](https://share.streamlit.io/)
    - Click 'Deploy an app' and then paste in your GitHub URL

Click to learn more about [how to use Streamlit Community Cloud.](https://docs.streamlit.io/streamlit-community-cloud)

## To Do
- [] Show how many blocks have been solo mined
- [] Show when someone solo mines and solves a block
  - [BTC.com](https://btc.com/stats/pool/Solo%20CK) currently shows the info above, but idk anything about them
