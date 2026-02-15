# Kehittäjäohje

## Rakenne

```
finnish-humanizer/
├── README.md                           ← Asennus, käyttö, esimerkit
├── LICENSE                             ← MIT
├── DEVELOPMENT.md                      ← Tämä tiedosto
├── finnish-humanizer/                  ← Kanoninen skill-sisältö
│   ├── SKILL.md                        ← Unified (portatiiviinen)
│   └── references/
│       └── patterns.md                 ← Täysi 26 kategorian patternilista + 4 tyylimerkintää
└── dist/                               ← Alustakohtaiset paketit
    ├── finnish-humanizer.zip            ← Claude.ai ZIP-upload
    ├── cursor/
    │   └── finnish-humanizer.mdc       ← Cursor (.cursor/rules/)
    └── copilot/
        └── finnish-humanizer.instructions.md  ← GitHub Copilot (.github/)
```

## Arkkitehtuuripäätökset

### Unified skill

Yksi kanoninen `SKILL.md` toimii kaikissa ympäristöissä (Claude.ai, Claude Code, API). CC-spesifiset kentät (kuten `argument-hint`) lisätään vain deployed CC-versioon. Alustakohtaiset paketit `dist/`-kansiossa muuttavat frontmatterin mutta säilyttävät bodyn.

| | Unified (kanoninen) | CC deployed | Cursor | Copilot |
|---|---|---|---|---|
| Frontmatter | `name`, `description`, `license`, `allowed-tools`, `metadata` | + `argument-hint` | `description`, `globs`, `alwaysApply` | `applyTo`, `description` |
| Body | Identtinen kaikilla | Identtinen | Identtinen (GitHub-linkit) | Identtinen (GitHub-linkit) |
| `references/` | Sisällytetty | Sisällytetty | Linkki GitHubiin | Linkki GitHubiin |

### Esimerkkien valinta (SKILL.md)

7 esimerkkiä valittu kattamaan:

- **4 suomenkielistä** (#1, #4, #5, #6) — skillin uniikki arvo, koska Claude tuntee universaalit patternit jo
- **3 universaalia** (#13, #15, #17) — yleisimmät, näyttävät miten korjaus toimii suomeksi

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

Body-sisältö on identtinen kaikissa dist-paketeissa. Kun muokkaat `SKILL.md`:n bodya:

1. Kopioi päivitetty body `dist/cursor/finnish-humanizer.mdc`:hen (vaihda `references/patterns.md` → GitHub-linkki)
2. Kopioi päivitetty body `dist/copilot/finnish-humanizer.instructions.md`:hen (sama muutos)
3. Päivitä ZIP:

```powershell
cd C:\Users\hassi\Projektit\Claude-Workflow\Skills-Dev\finnish-humanizer
Remove-Item dist\finnish-humanizer.zip -ErrorAction SilentlyContinue
Compress-Archive -Path finnish-humanizer -DestinationPath dist\finnish-humanizer.zip
```

### CC deployed version päivitys

Kopioi unified SKILL.md → `~/.claude/skills/finnish-humanizer/SKILL.md` ja lisää `argument-hint` frontmatteriin. Kopioi `references/patterns.md` vastaavasti.

## Verifiointi ennen julkaisua

| Tarkistus | Kriteeri |
|---|---|
| SKILL.md rivimäärä | < 160 |
| references/patterns.md | 26 patternia + 4 tyylimerkintää |
| Frontmatter-kentät | `name`, `description`, `license`, `allowed-tools`, `metadata` |
| Description-pituus | < 1024 merkkiä |
| XML-tagit | Jokainen avattu tagi suljetaan |
| Ei `finnish-naturalizer`-viittauksia | 0 osumaa koko projektissa |
| Ei `reference/`-viittauksia (yksikkö) | 0 osumaa koko projektissa |
| ZIP sisältö | `finnish-humanizer/SKILL.md` + `finnish-humanizer/references/patterns.md` |
| Cursor .mdc frontmatter | `description`, `globs`, `alwaysApply` |
| Copilot .instructions.md frontmatter | `applyTo`, `description` |
| Dist body synkroni | Body identtinen SKILL.md:n kanssa (paitsi references-linkki) |
