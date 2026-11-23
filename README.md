# Практика №5 — SysPulse

`syspulse` показывает uptime, среднюю нагрузку и сведения о памяти из `/proc`.
`syspulse --version` выводит версию.

## Настройка

1. На Mac с self-hosted раннером из ПР3 запустить Nexus 3.

   ```sh
   docker run -d --name nexus-pr5 -p 127.0.0.1:8081:8081 \
     -v nexus-pr5-data:/nexus-data sonatype/nexus3:latest
   ```

2. При первом входе пройти настройку Nexus Community Edition. Создать `apt (hosted)` с именем `syspulse`, дистрибутивом `stable` и политикой `Allow redeploy`. Включить анонимное чтение для APT и создать пользователя `deployer` с правами browse, read, add и edit на этот репозиторий.
3. Сгенерировать GPG-ключ для репозитория. В Nexus вставить закрытый ключ в поле Signing Key. Публичный ключ в формате ASCII armor сохранить в GitHub Actions variable `NEXUS_APT_KEY`.
4. В GitHub Actions Secrets добавить `NEXUS_HOST` (для Nexus на том же Mac — `127.0.0.1`), `NEXUS_USER` и `NEXUS_PASSWORD`.

## Проверка

Push в `release` запускает workflow. Он собирает бинарник Linux/amd64, упаковывает его с версией из `main.go`, публикует пакет и проверяет его установку через APT в новом контейнере Ubuntu 22.04. Пакет доступен в артефакте `syspulse-deb` на странице запуска. Workflow можно запустить повторно для той же версии.

[Документация Sonatype по APT](https://help.sonatype.com/en/apt-repositories.html)
