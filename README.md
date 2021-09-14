# KTrade

---

Welcome to KTrade. This app is still very much in active development, so expect big changes to how it works, and how the code is structured.
Currently the app is still pre-alpha so don't expect it to be a bug-free experience.

KTrade aims to simplify the process of entering/trimming/exiting your trades using Kristjans methods.

## What KTrade is

KTrade is a simple tool to aid you in getting the best entries for your trades. Its primary goal is to allow you to enter a trade with a
single button press, without the need to manually calculate your position sizing based on risk. KTrade will handle all of this for you,
so entering a trade should take a matter of seconds allowing you to get an entry as close to the breakout as possible

## What KTrade isn't (yet)

**An automated trading bot** - KTrade does NOT perform any automatic trading of any kind. One day it might respond to alerts and buy for you, but currently it has no automation

## Get started

The app is very early days so these instructions will change when a final release is ready. For now though

1. Clone the code from github
2. Install the dependencies

```shell
pip install -f requirements.txt
```

3. Prepare the database


```
flask db upgrade
```

4. Run the back end

```
flask run
```

5. In a separate terminal, run the front end (these won't always be separate)

```
yarn dev
```

6. Open your browser and go to

```
http://localhost:3000/initial_setup
```

Fill out the form, and save the details. Once done if you're not redirected automatically, go o

```
http://localhost:3000
```

7. Start playing around


### Notes

**Running the app**

**Important!** Please don't keep the app running 24/7!!

Currently the high/low tracking isn't feature complete, so it will keep the "low" of the day it started if it never goes below that.
This will mean the r/r calculations will be completely broken for every day after you started it.

Ensure you start the app the day you plan to trade.

This will be resolved in the future, but for now just shut it down.

**Pre-market**

The app has not been fully designed for placing pre-market orders. It is recommended you only place orders when the markets
are open. If you do not, then there are no guarantees it will work correctly.

### Contributors

- @Daniel H - Qullamaggie icons
- @Dolivent - Lots of ideas for what the app should do, now and in the future

### Enjoying KTrade and want to help?

If you're enjoying KTrade and want to help continue it's development, or just want to say thank you then you can sponsor me.

[:heart: Sponsor me](https://github.com/sponsors/pareeohnos)

### Contributing

