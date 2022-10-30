# Moraliser

A simple chat software with adult and slang filter

## Tags

- "Lojja korena"
- "Ainai giye bol beta"
- "Bolis kire"
- "Abar bol"
- "Pitiye debo"
- "Oslil"
- "Eh"
- "Yeaman"

## UI Design

<https://www.behance.net/gallery/93164379/Social-Concept-Application>

## Getting Started

- Clone the repository
- Install node modules

```bash
npm install
```

- Run the build create the distribution at `dist`.

```bash
npm run build
```

- Install python dependencies

```bash
pip install -r requirements.txt
```

- Initialise for database migration

```bash
flask db init
```

- To create db migration

```bash
flask db migrate -m "Added User Table"
```

- To run migration

```bash
flask db upgrade
```

