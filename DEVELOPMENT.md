# Kehittäjäohje

## Rakenne

```
finnish-humanizer/
├── README.md
├── LICENSE
├── DEVELOPMENT.md
├── build.py                            ← Build-skripti (generoi dist/)
├── finnish-humanizer/                  ← Kanoninen skill-sisältö
│   ├── SKILL.md                        ← Unified (portatiiviinen)
│   └── references/
│       └── patterns.md                 ← Täysi 26 kategorian patternilista + 5 tyylimerkintää
└── dist/                               ← Alustakohtaiset paketit (build-generoitu)
    ├── finnish-humanizer.zip            ← Claude.ai ZIP-upload
    ├── cursor/
    │   └── finnish-humanizer.mdc       ← Cursor (.cursor/rules/)
    ├── copilot/
    │   └── finnish-humanizer.instructions.md  ← GitHub Copilot (.github/)
    ├── windsurf/
    │   └── finnish-humanizer.md        ← Windsurf (.windsurfrules)
    ├── cline/
    │   └── finnish-humanizer.md        ← Cline (.cline/rules/)
    ├── continue/
    │   └── finnish-humanizer.md        ← Continue (.continue/rules/)
    ├── jetbrains/
    │   └── finnish-humanizer.md        ← JetBrains AI (.junie/rules/)
    ├── generic/
    │   └── finnish-humanizer.md        ← Aider, Bolt, Amazon Q, chat-alustat
    ├── agents/
    │   └── AGENTS.md                   ← Projektitason AI-agenttiohje
    └── chatgpt/
        ├── instructions.md             ← Custom GPT ohjeet (MANUAALINEN)
        ├── patterns.md                 ← Patternilista (build-generoitu)
        ├── GPT-SPEC.md                 ← GPT-konfiguraatio
        └── test-texts.md              ← Testiaineisto
```

## Arkkitehtuuripäätökset

### Unified skill

Yksi kanoninen `SKILL.md` toimii kaikissa ympäristöissä (Claude.ai, Claude Code, API). CC-spesifiset kentät (kuten `argument-hint`) lisätään vain deployed CC-versioon. Alustakohtaiset paketit `dist/`-kansiossa muuttavat frontmatterin mutta säilyttävät bodyn.

| | Unified (kanoninen) | CC deployed | Cursor | Copilot | Windsurf | Cline | Continue | JetBrains | Generic | Agents |
|---|---|---|---|---|---|---|---|---|---|---|
| Frontmatter | `name`, `description`, `license`, `allowed-tools`, `metadata` | + `argument-hint` | `description`, `globs`, `alwaysApply` | `applyTo`, `description` | Ei | Ei | `name`, `globs`, `alwaysApply`, `description` | Ei | Ei | Ei |
| Body | Identtinen kaikilla | Identtinen | Identtinen (GitHub-linkit) | Identtinen (GitHub-linkit) | Identtinen (GitHub-linkit) | Identtinen (GitHub-linkit) | Identtinen (GitHub-linkit) | Identtinen (GitHub-linkit) | Identtinen (GitHub-linkit) | Identtinen (GitHub-linkit) |
| `references/` | Sisällytetty | Sisällytetty | Linkki GitHubiin | Linkki GitHubiin | Linkki GitHubiin | Linkki GitHubiin | Linkki GitHubiin | Linkki GitHubiin | Linkki GitHubiin | Linkki GitHubiin |

### Esimerkkien valinta (SKILL.md)

7 esimerkkiä valittu kattamaan:

- **4 suomenkielistä** (#1, #4, #5, #6). Skillin uniikki arvo, koska Claude tuntee universaalit patternit jo
- **3 universaalia** (#13, #15, #17). Yleisimmät, näyttävät miten korjaus toimii suomeksi

Loput 19 patternia ovat `references/patterns.md`:ssä.

### XML-tagit

SKILL.md käyttää XML-tageja ylätason jäsentelyyn (`<role>`, `<finnish_voice>`, `<process>`, `<examples>`, `<output_format>`, `<constraints>`). Claude tulkitsee nämä rakenteellisina ohjeina, mikä parantaa ohjeiden noudattamista verrattuna pelkkiin markdown-otsikoihin. Cursor ja Copilot hyötyvät myös XML-tageista koska niiden LLM:t (GPT-4, Claude) ymmärtävät ne.

## Muokkaaminen

### Patternin lisääminen

1. Lisää pattern `references/patterns.md`:hen oikeaan kategoriaan (suomenkielinen / universaali)
2. Lisää Ennen/Jälkeen-esimerkit (vähintään yksi pari)
3. Päivitä sisällysluettelo
4. Jos pattern on erityisen yleinen tai tärkeä, harkitse sen lisäämistä myös `SKILL.md`:n 7 esimerkin joukkoon (korvaa vähiten hyödyllinen)

### Patternin muokkaaminen

Muokkaa suoraan relevanttia tiedostoa. Jos pattern esiintyy sekä `SKILL.md`:ssä että `references/patterns.md`:ssä, päivitä molemmat.

### Dist-pakettien päivitys

Kaikki dist-paketit generoidaan automaattisesti `build.py`-skriptillä:

```
py build.py
```

Skripti lukee `finnish-humanizer/SKILL.md`:n, erottaa frontmatterin ja bodyn, ja generoi alustakohtaiset tiedostot `dist/`-kansioon. Ainoa body-muutos: `ks. references/patterns.md` korvataan GitHub-URL:lla.

**Poikkeus:** `dist/chatgpt/instructions.md` on manuaalinen tiedosto (erilainen rakenne, ei XML-tageja, Kriittiset säännöt -osio). Se EI päivity `build.py`:llä. Tarkista synkroni manuaalisesti kun SKILL.md:n body muuttuu.

### build.py arkkitehtuuri

- **Lähde:** `finnish-humanizer/SKILL.md` (frontmatter + body)
- **Description:** Luetaan SKILL.md:n frontmatterista, lyhennetään 2 lauseeseen dist-käyttöön
- **Transformaatio:** `ks. references/patterns.md` → GitHub URL
- **ChatGPT patterns:** Kopioidaan `references/patterns.md`, poistetaan sisällysluettelo
- **ZIP:** Pakataan `finnish-humanizer/SKILL.md` + `finnish-humanizer/references/patterns.md`
- **Merkkirajojen tarkistus:** Windsurf max 12 000 merkkiä

### CC deployed version päivitys

Kopioi unified SKILL.md → `~/.claude/skills/finnish-humanizer/SKILL.md` ja lisää `argument-hint` frontmatteriin. Kopioi `references/patterns.md` vastaavasti.

## Verifiointi ennen julkaisua

| Tarkistus | Kriteeri |
|---|---|
| SKILL.md rivimäärä | < 160 |
| references/patterns.md | 26 patternia + 5 tyylimerkintää |
| Frontmatter-kentät | `name`, `description`, `license`, `allowed-tools`, `metadata` |
| Description-pituus | < 1024 merkkiä |
| XML-tagit | Jokainen avattu tagi suljetaan |
| Ei `finnish-naturalizer`-viittauksia | 0 osumaa koko projektissa |
| Ei `reference/`-viittauksia (yksikkö) | 0 osumaa koko projektissa |
| ZIP sisältö | `finnish-humanizer/SKILL.md` + `finnish-humanizer/references/patterns.md` |
| Cursor .mdc frontmatter | `description`, `globs`, `alwaysApply` |
| Copilot .instructions.md frontmatter | `applyTo`, `description` |
| Continue frontmatter | `name`, `globs`, `alwaysApply`, `description` |
| Windsurf merkkimäärä | < 12 000 |
| Dist body synkroni | Body identtinen SKILL.md:n kanssa (paitsi references-linkki) |
| `py build.py` | Ajo onnistuu, ei virheitä |
| ChatGPT instructions synkroni | Manuaalinen tarkistus kun SKILL.md body muuttuu |
