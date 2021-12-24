```
    ____       __                  _____        _
   / __ \___  / /__  ____ ________/__  /  _____(_)
  / /_/ / _ \/ / _ \/ __ `/ ___/ _ \/ /  / ___/ /
 / _, _/  __/ /  __/ /_/ (__  )  __/ /__/ /  / /
/_/ |_|\___/_/\___/\__,_/____/\___/____/_/  /_/

Meaningful and minimalist release notes for developers
```

Managing manual release notes is hard. Therefore, everyone tends to generate release notes from commit messages. But, you won't get a meaningful release note at the end. ReleaseZri offers you a simple strategy to maintain a human-friendly changelog and generate release notes automatically. It also gives you GitHub Action steps that you can simply copy-paste into your projects.

## Simple steps

- Use ReleaseZri's simple [changelog](CHANGELOG.md) format
- Create your own release note template in `.releasezri/template.md`
- Copy-paste `scripts/rz.py`
- Update your DevOps workflow to generate release notes via `scripts/rz.py create <version>` command

This project itself is maintained with ReleaseZri. Read documentation here: https://codezri.org/docs/releasezri

## Who use ReleaseZri?

- [ReleaseZri](https://github.com/codezri/releasezri)
- [Neutralinojs](https://neutralino.js.org)

## LICENSE

[MIT](LICENSE)
