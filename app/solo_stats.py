import streamlit as st
import pandas as pd

from load_data import get_user_data, load_pool_data, get_pool_data
from millify import millify

POOL_URL = f'https://solo.ckpool.org/pool/pool.status'

tab1, tab2, tab3 = st.tabs(["CKPool", "User", "Support Me"])

with tab1:

    # CKPool Data
    st.header('CKPool Data')
    st.markdown('Stats on CKPool')
    st.markdown(
        'Data acquired from [https://solo.ckpool.org/pool/pool.status](https://solo.ckpool.org/pool/pool.status)'
    )
    st.divider()

    ## Get and load CKPool data
    pool_data = get_pool_data(POOL_URL)
    # df = load_pool_data(pool_data)

    ## CKPool Participation Stats
    st.subheader('Participation')
    p1, p2, p3, p4 = st.columns(4)

    with p1:
        st.metric('Users', millify(pool_data['Users']))
    with p2:
        st.metric('Workers', millify(pool_data['Workers']))
    with p3:
        st.metric('Idle', millify(pool_data['Idle']))
    with p4:
        st.metric('Disconnected', millify(pool_data['Disconnected']))

    st.divider()

    st.subheader('Hashrate')
    hr1, hr2, hr3, hr4 = st.columns(4)

    ## CKPool Hashrate 
    with hr1:
        st.metric('Avg Hashrate (1m)', pool_data['hashrate1m'])
        st.metric('Avg Hashrate (6hr)', pool_data['hashrate6hr'])
    with hr2:
        st.metric('Avg Hashrate (5m)', pool_data['hashrate5m'])
        st.metric('Avg Hashrate (1d)', pool_data['hashrate1d'])
    with hr3:
        st.metric('Avg Hashrate (15m)', pool_data['hashrate15m'])
        st.metric('Avg Hashrate (7d)', pool_data['hashrate7d'])
    with hr4:
        st.metric('Avg Hashrate (1hr)', pool_data['hashrate1hr'])

    st.divider()

    ## Raw Data
    st.subheader('Raw Data')
    st.json(pool_data)

# User Stats
with tab2:

    # User Data
    st.header('User Data')
    user = st.text_input('Enter your CKPool user to get stats on your solo mining operation', key='user')
    USER_URL = f'https://solo.ckpool.org/users/{user}'

    st.markdown(
        'Data acquired from [https://solo.ckpool.org/users/{USER}](https://solo.ckpool.org/users/{USER})'
    )

    if user: 
        user_data = get_user_data(USER_URL)

        ## User Hashrate
        st.divider()
        st.subheader('Hashrate')
        hr1, hr2, hr3, hr4 = st.columns(4)
        with hr1:
            st.metric('Avg Hashrate (1m)', user_data['hashrate1m'])
            st.metric('Avg Hashrate (7d)', user_data['hashrate7d'])
        with hr2:
            st.metric('Avg Hashrate (5m)', user_data['hashrate5m'])
        with hr3:
            st.metric('Avg Hashrate (1hr)', user_data['hashrate1hr'])
        with hr4:
            st.metric('Avg Hashrate (1d)', user_data['hashrate1d'])

        st.divider()
        
        ## Raw Data
        st.subheader('Raw Data')
        st.json(user_data)
    
    ## Chance of solo mining a block
    st.divider()
    st.subheader('Solo Mining Chance Calculator')
    st.markdown('The odds of you solo mining a block')
    st.markdown(
        'Go to [https://solochance.com/](https://solochance.com/)'
    )


with tab3:
    st.header('Support')
    st.markdown("""
    If you find this streamlit app useful, consider 
    [supporting me with a few sats](https://strike.me/buddylasta/) 
    and [check out my website](https://www.jordanlaster.com).
    """)
    st.header('Run Locally')
    st.markdown("""
        Want to run this app on your own machine or in a docker container? [Check
        out the github repo](https://github.com/buddylasta/solo-viz).
        Feel free to contribute to the repo, fork it,
        or make your own changes.
    """)
    st.header('For more information...')
    st.markdown("""
        Check out [my youtube video on this dashboard](https://youtu.be/XfvF94boFAM)
    """)
