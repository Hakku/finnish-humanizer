# Finnish Humanizer

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-green.svg)](https://github.com/Hakku/finnish-humanizer/releases)
[![Platforms](https://img.shields.io/badge/alustat-15-purple.svg)](#tuetut-alustat)

Tunnistaa ja poistaa AI-generoidun suomenkielisen tekstin tunnusmerkit. Tekee tekstistä luonnollisempaa ja ihmisen kirjoittaman kuuloista.

## Ongelma

AI-generoitu suomi on tunnistettavaa: passiivin ylikäyttö, puuttuvat partikkelit, käännösrakenteet, mielistelevä sävy. Nämä patternit toistuvat kaikissa LLM:issä ja tekevät tekstistä robottimaisen.

## Ratkaisu

26 AI-patternia (12 suomenkielistä + 14 universaalia) ja 5 tyylimerkintää, joiden avulla teksti muunnetaan luonnolliseksi suomeksi. Ei käännä, ei yksinkertaista. Poistaa vain AI-tunnusmerkit ja tuo kirjoittajan äänen esiin.

**Ennen:**
> Tämä on erittäin merkittävä kehitysaskel, joka tulee vaikuttamaan laajasti alan tulevaisuuteen. On syytä huomata, että kyseinen innovaatio tarjoaa lukuisia mahdollisuuksia eri sidosryhmille.

**Jälkeen:**
> Iso juttu alalle. Tästä hyötyvät monet.

Täysi patternilista esimerkkeineen: [`finnish-humanizer/references/patterns.md`](finnish-humanizer/references/patterns.md)

## Tuetut alustat

| Alusta | Tyyppi | Tiedosto |
|--------|--------|----------|
| Claude Code | Editori | `finnish-humanizer/SKILL.md` |
| Cursor | Editori | `dist/cursor/finnish-humanizer.mdc` |
| GitHub Copilot | Editori | `dist/copilot/finnish-humanizer.instructions.md` |
| Windsurf | Editori | `dist/windsurf/finnish-humanizer.md` |
| Cline | Editori | `dist/cline/finnish-humanizer.md` |
| Continue | Editori | `dist/continue/finnish-humanizer.md` |
| JetBrains AI | Editori | `dist/jetbrains/finnish-humanizer.md` |
| Aider | Editori | `dist/generic/finnish-humanizer.md` |
| Bolt.new | Editori | `dist/generic/finnish-humanizer.md` |
| Amazon Q | Editori | `dist/generic/finnish-humanizer.md` |
| Claude.ai | Chat | `dist/finnish-humanizer.zip` |
| ChatGPT | Chat | Custom GPT / `dist/generic/` |
| Gemini Gems | Chat | `dist/generic/finnish-humanizer.md` |
| Perplexity Spaces | Chat | `dist/generic/finnish-humanizer.md` |
| AGENTS.md | Cross | `dist/agents/AGENTS.md` |

## Asennus

### Koodieditorit

<details>
<summary><strong>Claude Code</strong></summary>

1. Kopioi `finnish-humanizer/`-kansio (sisältää `SKILL.md` + `references/`) polkuun `~/.claude/skills/finnish-humanizer/`
2. Käynnistä Claude Code uudelleen
3. Kutsu: `/finnish-humanizer [tiedostopolku tai teksti]`

**CC-lisäasetukset:** Lisää frontmatteriin `argument-hint: "[tiedostopolku tai teksti]"` saadaksesi käyttövinkin slash-komennon yhteyteen.

</details>

<details>
<summary><strong>Cursor</strong></summary>

1. Kopioi `dist/cursor/finnish-humanizer.mdc` projektin `.cursor/rules/`-kansioon
2. Skill aktivoituu automaattisesti `.md`- ja `.txt`-tiedostoille

</details>

<details>
<summary><strong>GitHub Copilot</strong></summary>

1. Kopioi `dist/copilot/finnish-humanizer.instructions.md` projektin `.github/`-kansioon
2. Copilot injektoi ohjeet automaattisesti `.md`- ja `.txt`-tiedostoille

</details>

<details>
<summary><strong>Windsurf</strong></summary>

1. Kopioi `dist/windsurf/finnish-humanizer.md` projektin `.windsurfrules/`-kansioon
2. Tai lisää globaalisti: Windsurf Settings → Rules → lisää tiedoston sisältö

</details>

<details>
<summary><strong>Cline</strong></summary>

1. Kopioi `dist/cline/finnish-humanizer.md` projektin `.cline/rules/`-kansioon
2. Tai lisää Cline-asetuksista: Custom Instructions → liitä tiedoston sisältö

</details>

<details>
<summary><strong>Continue</strong></summary>

1. Kopioi `dist/continue/finnish-humanizer.md` projektin `.continue/rules/`-kansioon
2. Ohjeet aktivoituvat automaattisesti `.md`- ja `.txt`-tiedostoille (`globs`-kentän perusteella)

</details>

<details>
<summary><strong>JetBrains AI</strong></summary>

1. Kopioi `dist/jetbrains/finnish-humanizer.md` projektin `.junie/rules/`-kansioon (Junie)
2. Tai AI Assistant: Settings → AI Assistant → Project-level prompt → liitä sisältö

</details>

<details>
<summary><strong>Aider</strong></summary>

```
aider --read dist/generic/finnish-humanizer.md
```

Lisää `references/patterns.md` tarvittaessa:

```
aider --read dist/generic/finnish-humanizer.md --read finnish-humanizer/references/patterns.md
```

</details>

<details>
<summary><strong>Bolt.new</strong></summary>

1. Avaa projekti Bolt.new:ssa
2. Liitä `dist/generic/finnish-humanizer.md`:n sisältö **Project Prompt** -kenttään

</details>

<details>
<summary><strong>Amazon Q</strong></summary>

1. Kopioi `dist/generic/finnish-humanizer.md` projektin `.amazonq/rules/`-kansioon
2. Amazon Q lukee ohjeet automaattisesti

</details>

### Chat-alustat

<details>
<summary><strong>Claude.ai (projekti)</strong></summary>

1. [Lataa `finnish-humanizer.zip`](https://github.com/Hakku/finnish-humanizer/releases/latest/download/finnish-humanizer.zip) (tai `dist/finnish-humanizer.zip` reposta)
2. Avaa [claude.ai](https://claude.ai) ja luo uusi projekti
3. Lisää ZIP projektin **Project knowledge** -osioon

Vaihtoehtoisesti: kopioi `finnish-humanizer/SKILL.md`:n sisältö projektin **Custom instructions** -kenttään ja lisää `references/patterns.md` tiedostona.

</details>

<details>
<summary><strong>ChatGPT</strong></summary>

**Custom GPT (valmis):** [Finnish Humanizer — Luonnollista suomea](https://chatgpt.com/g/g-69930f3ef1bc8191b2b998e0e01dc99e-finnish-humanizer-luonnollista-suomea) (vaatii Plus/Pro)

**ChatGPT Projects:**
1. Luo uusi projekti ChatGPT:ssä
2. Lataa `dist/generic/finnish-humanizer.md` ja `finnish-humanizer/references/patterns.md` projektin tiedostoiksi
3. Ohjeet aktivoituvat projektin keskusteluissa

</details>

<details>
<summary><strong>Gemini Gems</strong></summary>

1. Avaa [Gemini](https://gemini.google.com) → Gem Manager → Create
2. Liitä `dist/generic/finnish-humanizer.md`:n sisältö Gem-ohjeiksi
3. Lataa `finnish-humanizer/references/patterns.md` liitteeksi
4. Tallenna ja käytä Gemiä keskustelussa

</details>

<details>
<summary><strong>Perplexity Spaces</strong></summary>

1. Luo uusi Space [Perplexity](https://perplexity.ai):ssä
2. Lataa `dist/generic/finnish-humanizer.md` ja `finnish-humanizer/references/patterns.md` Spacen tiedostoiksi
3. Ohjeet vaikuttavat Spacen keskusteluissa

</details>

### Cross-platform

<details>
<summary><strong>AGENTS.md</strong></summary>

Projektitason AI-agenttiohjeet. Kopioi `dist/agents/AGENTS.md` projektin juureen. Kaikki AI-agentit (Claude Code, Cursor, Copilot jne.) tunnistavat AGENTS.md-tiedostoja ja lukevat ne automaattisesti.

</details>

<details>
<summary><strong>API (system prompt)</strong></summary>

Lisää `finnish-humanizer/SKILL.md`:n sisältö system-promptiin ja `references/patterns.md` kontekstina.

</details>

## Käyttö

Liitä suomenkielinen teksti ja pyydä luonnollistamaan:

```
Luonnollista tämä teksti:

[tekstisi tähän]
```

Muita toimivia komentoja:

- "Poista AI-tuntu tästä tekstistä"
- "Tee tästä ihmismäisempää"
- "Humanisoi tämä"

### Analysointi vs. suora korjaus

- **Oletus:** Luonnollistaa tekstin suoraan ja palauttaa korjatun version + muutosyhteenvedon.
- **"Analysoi ensin":** Palauttaa vain löydetyt AI-patternit ilman korjauksia, voit valita mitkä korjataan.

### Muutosyhteenveto

Oletuksena skill palauttaa tekstin lisäksi lyhyen listan tehdyistä muutoksista. Jos haluat pelkän tekstin:

```
Luonnollista tämä teksti. Älä selitä muutoksia.
```

## Rajoitukset

- Toimii vain suomenkieliselle tekstille
- Ei muuta asiasisältöä, vain esitystapaa
- Ei yksinkertaista, virallinen teksti pysyy virallisena
- Ei korvaa ihmisen editointia, poistaa AI-tunnusmerkkejä, ei tee tekstistä "hyvää"

## Lisenssi

MIT. Katso [LICENSE](LICENSE)
