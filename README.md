# Finnish Humanizer

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/Hakku/finnish-humanizer/releases)
[![Platforms](https://img.shields.io/badge/platforms-Claude%20%7C%20ChatGPT%20%7C%20Cursor%20%7C%20Copilot-purple.svg)](#asennus)

Tunnistaa ja poistaa AI-generoidun suomenkielisen tekstin tunnusmerkit. Tekee tekstistä luonnollisempaa ja ihmisen kirjoittaman kuuloista.

## Ongelma

AI-generoitu suomi on tunnistettavaa: passiivin ylikäyttö, puuttuvat partikkelit, käännösrakenteet, mielistelevä sävy. Nämä patternit toistuvat kaikissa LLM:issä ja tekevät tekstistä robottimaisen.

## Ratkaisu

26 AI-patternia (12 suomenkielistä + 14 universaalia) ja 4 tyylimerkintää, joiden avulla teksti muunnetaan luonnolliseksi suomeksi. Ei käännä, ei yksinkertaista — poistaa vain AI-tunnusmerkit ja tuo kirjoittajan äänen esiin.

**Ennen:**
> Tämä on erittäin merkittävä kehitysaskel, joka tulee vaikuttamaan laajasti alan tulevaisuuteen. On syytä huomata, että kyseinen innovaatio tarjoaa lukuisia mahdollisuuksia eri sidosryhmille.

**Jälkeen:**
> Iso juttu alalle. Tästä hyötyvät monet.

Täysi patternilista esimerkkeineen: [`finnish-humanizer/references/patterns.md`](finnish-humanizer/references/patterns.md)

## Asennus

### Claude Code

1. Kopioi `finnish-humanizer/`-kansio (sisältää `SKILL.md` + `references/`) polkuun `~/.claude/skills/finnish-humanizer/`
2. Käynnistä Claude Code uudelleen
3. Kutsu: `/finnish-humanizer [tiedostopolku tai teksti]`

**CC-lisäasetukset:** Lisää frontmatteriin `argument-hint: "[tiedostopolku tai teksti]"` saadaksesi käyttövinkin slash-komennon yhteyteen.

### Claude.ai (projekti)

1. [Lataa `finnish-humanizer.zip`](https://github.com/Hakku/finnish-humanizer/releases/latest/download/finnish-humanizer.zip) (tai `dist/finnish-humanizer.zip` reposta)
2. Avaa [claude.ai](https://claude.ai) ja luo uusi projekti
3. Lisää ZIP projektin **Project knowledge** -osioon

Vaihtoehtoisesti: kopioi `finnish-humanizer/SKILL.md`:n sisältö projektin **Custom instructions** -kenttään ja lisää `references/patterns.md` tiedostona.

### Cursor

1. Kopioi `dist/cursor/finnish-humanizer.mdc` projektin `.cursor/rules/`-kansioon
2. Skill aktivoituu automaattisesti `.md`- ja `.txt`-tiedostoille

### ChatGPT (Custom GPT)

Käytä valmista GPT:tä suoraan: **[Finnish Humanizer — Luonnollista suomea](https://chatgpt.com/g/g-69930f3ef1bc8191b2b998e0e01dc99e-finnish-humanizer-luonnollista-suomea)**

Vaatii ChatGPT Plus/Pro -tilauksen.

### GitHub Copilot

1. Kopioi `dist/copilot/finnish-humanizer.instructions.md` projektin `.github/`-kansioon
2. Copilot injektoi ohjeet automaattisesti `.md`- ja `.txt`-tiedostoille

### API (`container.skills`)

Lisää `finnish-humanizer/SKILL.md`:n sisältö system-promptiin ja `references/patterns.md` kontekstina.

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
- **"Analysoi ensin":** Palauttaa vain löydetyt AI-patternit ilman korjauksia — voit valita mitkä korjataan.

### Muutosyhteenveto

Oletuksena skill palauttaa tekstin lisäksi lyhyen listan tehdyistä muutoksista. Jos haluat pelkän tekstin:

```
Luonnollista tämä teksti. Älä selitä muutoksia.
```

## Rajoitukset

- Toimii vain suomenkieliselle tekstille
- Ei muuta asiasisältöä — vain esitystapaa
- Ei yksinkertaista — virallinen teksti pysyy virallisena
- Ei korvaa ihmisen editointia — poistaa AI-tunnusmerkkejä, ei tee tekstistä "hyvää"

## Lisenssi

MIT — katso [LICENSE](LICENSE)
