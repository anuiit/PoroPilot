<h1 align="center">💫 PoroPilot 💫</h1>

🚀 **Features**

PoroPilot is a Python library designed to simplify interactions with the Riot Games API.

- **PoroPilot**: Your primary interface to the Riot API, handling initialization of essential details like the API key and region.

- **RequestHandler**: Manages the creation of requests, utilizing `UrlBuilder` for URL setup and manages 429 (rate limit) errors.

- **Endpoints**: Each primary endpoint houses a variety of sub-endpoints, see more here [RiotAPI](https://developer.riotgames.com/apis).

<br>

🛠️ Usage

*For a more detailed documentation : [Here](https://anuiit.github.io/poropilot-docs/)*

Here's a quick start guide to get you up and running:

Install PoroPilot using pip:
    
        pip install PoroPilot

To start interacting with the Riot API, initialize the `PoroPilot` class with your API key and the desired region. Here's a simple example to get summoner and match information:

        from PoroPilot import PoroPilot
        
        poro_kr = PoroPilot("RGAPI-XXXXX", "kr")
        poro_euw = PoroPilot("RGAPI-XXXXX", "euw1")
        
        print(poro_kr.summoner.by_name("hideonbush"))
        print(poro_kr.match.by_match_id("KR_6965060843"))
        
        print(poro_euw.summoner.by_name("zyb"))
        print(poro_euw.match.by_match_id("EUW1_6830353289"))

PoroPilot maps directly to Riot API's endpoints with function names that mirror the official ones.

<br>

🚀 **Future Improvements**

A range of improvements are planned, including:

- [ ] **Automatic Region Search**

- [ ] **Refactor Endpoints into a Main API Class**

- [ ] **Expanded API Coverage**

- [ ] **In Depth Examples**
