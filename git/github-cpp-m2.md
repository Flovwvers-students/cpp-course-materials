# GitHub на паре: C++ — М2

Организация: https://github.com/Flovwvers-students. Один именной репозиторий на студента. Все стартовые проекты одного языка одинаковы.

## Видимость и доступ

Репозитории приватные. В организации Base permissions установлен в No permission: само членство не открывает чужие репозитории. Преподаватель выдаёт студенту Admin в его именном репозитории, студент приглашает выбранных разработчика и ревьюера с Write. Отдельные права пользователей и команд сохраняются. Владельцы организации видят все репозитории. На плане GitHub Free обязательное ревью через rulesets в приватных репозиториях недоступно: процесс PR/review соблюдается по договорённости; для технического ограничения нужен подходящий платный план.

## 1. Что вы будете делать

Для первого этапа каждому студенту выделен **именной репозиторий** в организации Flovwvers-students. Все стартовые проекты одного языка одинаковы: калькулятор со сложением и вычитанием. Каждый проходит три роли — аналитик, разработчик, ревьюер — вместе с двумя одногруппниками.

Названия: `java-calculator-фамилия-имя` для М3 и `cpp-calculator-фамилия-имя` для М2, латиницей. Например, `java-calculator-belyakov-aleksey`. Если в исходном списке только инициалы, они сохранены: `java-calculator-deyneka-d-a`. Адрес своего репозитория возьмите из таблицы преподавателя, не угадывайте транслитерацию.

### Как организовать три роли

Соберитесь втроём: A, B и C. У каждого есть свой именной репозиторий. Согласуйте роли между собой:

| Репозиторий | Аналитик и администратор | Разработчик | Ревьюер |
|---|---|---|---|
| Репозиторий A | A | B | C |
| Репозиторий B | B | C | A |
| Репозиторий C | C | A | B |

Это пример договорённости, а не заранее назначенные преподавателем участники. Студенты сами выбирают команду и добавляют её в свой репозиторий. Преподаватель не создаёт учебные Issue/PR за студентов и не назначает исполнителей или ревьюеров.

Можно выполнять три репозитория по очереди с ротацией или идти по этапам: все создают задачи как аналитики, все реализуют чужую задачу как разработчики, затем все проверяют чужой PR. В результате каждый сделал один полный набор действий в каждой роли. Если группа не делится на три, согласуйте с преподавателем участие одного человека в двух командах; автор кода и его ревьюер всегда разные люди.

### Права и самостоятельное добавление команды

Преподаватель позже добавляет студента в его именной репозиторий с правом **Admin**. Admin действует в этом репозитории, а не означает Owner всей организации. Репозитории можно подготовить до регистрации и приглашения всех студентов.

После получения Admin студент-аналитик сам приглашает разработчика и ревьюера с правом **Write** через Settings → Collaborators and teams → Add people. Аналитику здесь нужен Admin именно для самостоятельного управления командой; схема с Triage на первом этапе не используется. Разработчик и ревьюер принимают приглашения, после чего начинают работу.

Защита main требует PR и чужого одобрения, если включена. Не изменяйте и не отключайте её на занятии. Admin даёт возможность управлять настройками, поэтому соблюдение правил также является ответственностью студента. Слияние после проверки выполняет ревьюер; технически Write может позволить автору нажать Merge после чужого одобрения, но на занятии так не делаем.

## 2. Аккаунт и подготовка

1. Откройте https://github.com, создайте аккаунт, подтвердите почту. Если аккаунт уже есть, используйте его.
2. Включите двухфакторную защиту в Settings → Password and authentication.
3. Сообщите преподавателю **логин**, не пароль и не токен. ФИО в Excel не является логином GitHub.
4. Примите приглашение в свой именной репозиторий с правом Admin. Затем примите приглашения в репозитории, где вас выбрали разработчиком или ревьюером.
5. На университетском ПК найдите личный сохраняемый диск и проверьте предустановленные программы по разделу 3. На собственном ноутбуке установите необходимые программы. После установки заново откройте терминал.
6. Используйте редактор кода (например, уже установленный VS Code). Сохраняйте файлы UTF-8 с указанными расширениями, без дополнительного `.txt`.

Git — программа на компьютере, GitHub — сайт, commit — локальное сохранение изменений, push — отправка коммитов на сервер. Pull Request — запрос на включение ветки в main; Issue — описание задачи.

## 3. Git, компилятор и вход

### Университетский компьютер: личный диск и новая сессия

На компьютерах университета используйте предустановленные Git и IDE. Не выполняйте команды установки ниже: установка ПО и недостающего JDK/компилятора — задача преподавателя или администратора. IntelliJ IDEA может быть установлена отдельно от JDK; проверьте доступный Project SDK.

После входа под университетским логином часть настроек профиля может восстанавливаться. Точный механизм уточняется у администратора. Не рассчитывайте, что Рабочий стол, Downloads, папка пользователя или произвольная папка на C: сохранятся. Исходники, `.git` и проекты храните на своём сохраняемом диске.

Откройте «Этот компьютер», найдите именно личный диск с вашим именем. Буква может различаться: Z: ниже — только пример. Уточните у преподавателя, какой диск сохраняется после выхода; чужой или общий диск не выбирайте. Посмотреть подключённые диски:

PowerShell:

```powershell
Get-PSDrive -PSProvider FileSystem | Select-Object Name,Root,DisplayRoot
net use
```

CMD:

```bat
net use
echo %HOMEDRIVE%
echo %HOMESHARE%
```

После подтверждения диска создайте на нём папку `github`. В примерах замените Z: своей буквой. Выполняйте этот блок в каждом новом терминале после входа, до `git config --global` и clone:

PowerShell:

```powershell
$UniversityGithub = 'Z:\github'
if (-not (Test-Path 'Z:\')) { throw 'Личный диск не подключён: уточните букву' }
New-Item -ItemType Directory -Force $UniversityGithub | Out-Null
Set-Location $UniversityGithub
$env:GIT_CONFIG_GLOBAL = Join-Path $UniversityGithub '.gitconfig'
git --version
```

CMD (если диск недоступен, остановитесь и уточните букву):

```bat
dir Z:\
set "UniversityGithub=Z:\github"
if not exist "%UniversityGithub%" mkdir "%UniversityGithub%"
cd /d "%UniversityGithub%"
set "GIT_CONFIG_GLOBAL=%UniversityGithub%\.gitconfig"
git --version
```

`GIT_CONFIG_GLOBAL` указывает Git на ваш файл настроек на личном диске. Поэтому следующие команды `git config --global` сохранят имя, почту и учебный прокси там. Сама переменная действует только в текущем терминале: после нового входа или открытия другого терминала задайте её снова. В терминале IntelliJ выполните тот же блок. На личном ноутбуке этот блок не нужен: используйте обычный файл настроек Git.

Не записывайте пароль, токен или пароль прокси в `.gitconfig`, URL или файл на сетевом диске. Вход GitHub через браузер и хранилище учётных данных может потребоваться повторить после новой сессии. Откройте проект IDE из папки личного диска, при необходимости заново выберите SDK. Если Git или компилятор не найден, сообщите преподавателю; не меняйте системные настройки и не устанавливайте ПО самостоятельно.

### Установка на личном ноутбуке

Следующие команды относятся к собственному компьютеру. На университетском ПК переходите к проверке и данным автора.

### Windows: PowerShell

```powershell
winget install --id Git.Git -e
```

### Windows: CMD

```bat
winget install --id Git.Git -e
```

Для C++ на Windows установите MSYS2 с https://www.msys2.org. В его терминале **MSYS2 UCRT64** выполните:

```sh
pacman -S --needed mingw-w64-ucrt-x86_64-gcc
```

В PowerShell добавьте путь на текущую сессию: `$env:Path = "C:\msys64\ucrt64\bin;" + $env:Path`. В CMD: `set "PATH=C:\msys64\ucrt64\bin;%PATH%"`. Если MSYS2 установлен иначе, исправьте путь. Для постоянного использования добавьте эту папку в пользовательский Path через настройки Windows.

### Linux (Ubuntu/Debian)

```sh
sudo apt update
sudo apt install git g++
```

Для других дистрибутивов используйте их пакетный менеджер.

### macOS

```sh
xcode-select --install
```

На macOS установка Command Line Tools даёт Git и clang++. Если winget недоступен, скачайте Git с https://git-scm.com/downloads.

### Проверка и данные автора

Команды одинаковы в PowerShell, CMD и Linux/macOS:

```sh
git --version
g++ --version
git config --global user.name "Фамилия Имя"
git config --global user.email "ВАША-ПОЧТА-GITHUB"
git config --global init.defaultBranch main
git config --global core.quotepath false
```

На macOS проверьте `clang++ --version`; при сборке ниже замените `g++` на `clang++`.

Указывайте свою почту GitHub или noreply-адрес из Settings → Emails. Имя автора коммита не выдаёт права в репозитории.

### Вход для HTTPS

На Windows Git for Windows обычно включает Git Credential Manager: при первом push пройдите вход GitHub в браузере. На Linux/macOS можно установить GitHub CLI по https://cli.github.com и выполнить:

```sh
gh auth login -h github.com -p https -w
gh auth setup-git
```

Эти команды также работают в PowerShell и CMD, если gh установлен. Не отправляйте пароль/токен преподавателю. SSH-ключ для HTTPS не нужен. Если сеть не работает, сначала раздел 4.

## 4. Если Git не подключается: Windows 10 и прокси

Этот раздел выполняйте **до clone**, если сеть университета требует прокси или появляется timeout. Открытие GitHub в браузере ещё не означает, что Git использует те же настройки. Прокси браузера/Windows, WinHTTP, переменные окружения и настройки Git могут различаться.

Сначала проверьте сеть без добавления новых настроек. Одинаково в PowerShell и CMD:

```sh
git ls-remote --heads https://github.com/git/git.git
```

Это публичный проект Git: проверка не требует доступа к учебному репозиторию. Если появились хеши веток, переходите к clone своего проекта; прокси без причины не добавляйте. Команда использует уже действующие настройки Git и окружения. При timeout или ошибке подключения выполняйте диагностику ниже. При `Repository not found` у приватного учебного проекта проверьте HTTPS-адрес, вход нужным аккаунтом и принятие приглашения; повторная настройка прокси сама по себе прав не выдаёт. Команды не должны ссылаться на старый общий `java-calculator-01`.

### 4.1. Получить текущие настройки

Выберите блок для своей оболочки. Команды ниже читают настройки; ничего не меняют. Вывод может содержать пароль, поэтому перед отправкой преподавателю замажьте учётные данные.

**PowerShell (Windows):**

```powershell
netsh winhttp show proxy
Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings' | Select-Object ProxyEnable,ProxyServer,ProxyOverride,AutoConfigURL
Get-ChildItem Env: | Where-Object Name -Match '^(HTTP_PROXY|HTTPS_PROXY|ALL_PROXY|NO_PROXY)$'
git config --show-origin --get-regexp '.*proxy.*'
git config --get-urlmatch http.proxy https://github.com
Test-NetConnection github.com -Port 443
```

**CMD (Windows):**

```bat
netsh winhttp show proxy
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyEnable
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyServer
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v ProxyOverride
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v AutoConfigURL
set | findstr /I "HTTP_PROXY HTTPS_PROXY ALL_PROXY NO_PROXY"
git config --show-origin --get-regexp ".*proxy.*"
git config --get-urlmatch http.proxy https://github.com
curl.exe -I --connect-timeout 15 https://github.com
```

Как читать результат:

- `ProxyEnable=1` и `ProxyServer` вида `proxy.university.example:8080` дают адрес и порт. Значение `http=...;https=...` задаёт отдельные серверы для разных протоколов.
- `Direct access` у WinHTTP не доказывает отсутствие прокси в браузере.
- `AutoConfigURL`/PAC — **адрес файла правил**, а не прокси-сервера. Git не принимает `.pac` как значение `http.proxy`. Администратор должен сообщить сервер и порт, выбранные PAC для `github.com`; не угадывайте их.
- Отсутствие вывода у `git config --get-regexp` или `--get-urlmatch` с кодом 1 означает, что настройка не найдена.
- `NO_PROXY`/`no_proxy` может исключать GitHub из прокси. Проверьте его, если Git продолжает подключаться напрямую.

### 4.2. Проверить найденный прокси без постоянного изменения

Замените `proxy.university.example:8080` **своим** адресом. Это пример, он не заработает буквально.

**PowerShell:**

```powershell
git -c http.proxy="http://proxy.university.example:8080" ls-remote --heads https://github.com/git/git.git
```

**CMD:**

```bat
git -c http.proxy="http://proxy.university.example:8080" ls-remote --heads https://github.com/git/git.git
```

В ответе должны быть хеши и `refs/heads/...`. Здесь используется публичный репозиторий проекта Git для проверки сети, а не ваш учебный проект. `http://` у прокси допустим и при обращении к `https://github.com`: через HTTP CONNECT устанавливается TLS-соединение к GitHub. Для SOCKS-прокси используйте, например, `socks5h://127.0.0.1:1080`, только если это реальный адрес вашего запущенного прокси; `socks5h` передаёт разрешение DNS прокси-серверу.

### 4.3. Сохранить прокси только для GitHub

Ниже команды для PowerShell и CMD. Прокси на Linux/macOS вынесен в раздел 14 в конце файла.

**PowerShell:**

```powershell
git config --global http.https://github.com.proxy "http://proxy.university.example:8080"
git config --get-urlmatch http.proxy https://github.com
```

**CMD:**

```bat
git config --global http.https://github.com.proxy "http://proxy.university.example:8080"
git config --get-urlmatch http.proxy https://github.com
```

Git использует параметр `http.proxy` и для HTTPS. Отдельный параметр Git `https.proxy` для этого создавать не нужно. Для всех HTTP(S)-репозиториев вместо настройки по URL существует `git config --global http.proxy "http://HOST:PORT"`, но на занятии достаточно настройки для GitHub.

Альтернатива — переменные **только текущей сессии**. Они действуют шире, чем настройка только GitHub, и могут использоваться другими программами. Не смешивайте способы без необходимости.

**PowerShell:**

```powershell
$env:HTTP_PROXY = 'http://proxy.university.example:8080'
$env:HTTPS_PROXY = 'http://proxy.university.example:8080'
```

**CMD:**

```bat
set "HTTP_PROXY=http://proxy.university.example:8080"
set "HTTPS_PROXY=http://proxy.university.example:8080"
```

### 4.4. Вернуться к прямому подключению

Удаляйте только настройки, которые добавили на занятии. Сначала сохраните старые значения, если они были. Чтобы убрать прокси только GitHub:

**PowerShell:**

```powershell
git config --global --unset-all http.https://github.com.proxy
Remove-Item Env:HTTP_PROXY,Env:HTTPS_PROXY -ErrorAction SilentlyContinue
```

**CMD:**

```bat
git config --global --unset-all http.https://github.com.proxy
set HTTP_PROXY=
set HTTPS_PROXY=
```

Если сами задавали общий `http.proxy`, уберите его через `git config --global --unset-all http.proxy`. Значения из системного или локального файла могут продолжить действовать: `--show-origin` показывает источник. Не удаляйте чужие настройки вслепую. `ALL_PROXY` и `NO_PROXY` проверяются отдельно.

### 4.5. Прокси и авторизация — разные проблемы

| Ошибка | Что делать |
|---|---|
| Could not resolve proxy | Проверить имя прокси, подключение к сети университета/VPN и DNS |
| Failed to connect / timeout | Проверить сервер и порт, работает ли прокси и разрешён ли GitHub |
| 407 Proxy Authentication Required | Прокси требует входа; уточнить у администратора механизм (NTLM, Negotiate и др.) и поддержку Git. Пароль не записывать в URL, историю команд или репозиторий |
| SSL certificate problem | Получить у администратора доверенный корневой сертификат и настроить доверие к нему. Не использовать `http.sslVerify=false` и `curl -k` |
| 403 / 404 при push | Проверить аккаунт, адрес репозитория, принятые приглашения и право Write; 404 также может скрывать отсутствие доступа |
| Authentication failed | Для GitHub HTTPS нужен credential manager/вход браузером или токен; пароль аккаунта GitHub не заменяет токен |

Настройка `http.proxy` не влияет на SSH-адрес `git@github.com:...`. Для этой инструкции используйте **HTTPS**. Если уже клонировали по SSH, внутри проекта замените адрес на HTTPS своего репозитория:

```sh
git remote -v
git remote set-url origin https://github.com/Flovwvers-students/ИМЯ-РЕПОЗИТОРИЯ.git
```

Эти две команды одинаковы в PowerShell, CMD и Linux/macOS. Не отключайте проверку сертификатов ради подключения.

## 5. Аналитик: собрать команду и создать Issue

1. Откройте свой именной репозиторий. Согласуйте с двумя одногруппниками, кто будет разработчиком, а кто ревьюером. Узнайте их точные GitHub-логины.
2. Откройте **Settings → Collaborators and teams → Add people**, найдите разработчика по логину, выберите **Write** и отправьте приглашение. Повторите для ревьюера. Название раздела может отображаться как Collaborators или Manage access. Если политика организации запрещает приглашать внешних участников, попросите преподавателя сначала добавить их в организацию; затем пригласите их в свой репозиторий сами.
3. Дождитесь, пока оба примут приглашения. Проверьте список collaborators. Если нет Settings или Add people, преподаватель ещё не выдал вам Admin. Admin даётся только вам в вашем репозитории; команде для разработки и проверки достаточно Write.
4. Откройте репозиторий → **Issues → New issue**. Если предложен шаблон, выберите **Open a blank issue**.
5. Заголовок: `Добавить умножение в калькулятор`. Вставьте описание:

```markdown
## Контекст
В калькуляторе уже есть сложение и вычитание. Нужно добавить умножение.

## Критерии приёмки
- [ ] В src/Calculator.hpp есть публичный метод multiply(int left, int right), возвращающий int.
- [ ] multiply(5, 3) = 15; multiply(0, 7) = 0; multiply(-2, 3) = -6.
- [ ] При запуске показана строка 5 * 3 = 15.
- [ ] Строки Calculator, 5 - 3 = 2 и 5 + 3 = 8 сохранены.
- [ ] Проект собирается без ошибок.

## Границы задачи
Только небольшие целые числа. Деление, дроби и переполнение не входят в задачу.
```

6. Справа **Assignees** → выберите выбранного вами разработчика этого репозитория. При наличии метки выберите `enhancement`. Если нет Assignees или нужного логина, проверьте права с преподавателем.
7. Нажмите **Submit new issue**. Сообщите разработчику ссылку и номер (например, #1).

## 6. Разработчик: ветка и код

1. Откройте назначенное Issue в **чужом** репозитории, прочитайте критерии, напишите «Беру в работу».
2. Скопируйте HTTPS-адрес через **Code → Local → HTTPS**. В командах ниже показан пример; замените его на репозиторий, где вы разработчик.

На университетском ПК сначала выполните блок личного диска из раздела 3 в этом терминале. На собственном Windows-ноутбуке вместо `Set-Location $UniversityGithub` используйте `New-Item -ItemType Directory -Force "$HOME/github" | Out-Null`, затем `Set-Location "$HOME/github"`; в CMD вместо пути переменной — `if not exist "%USERPROFILE%\github" mkdir "%USERPROFILE%\github"`, затем `cd /d "%USERPROFILE%\github"`. Остальные команды clone и создания ветки одинаковы.

PowerShell:

```powershell
Set-Location $UniversityGithub
git clone https://github.com/Flovwvers-students/cpp-calculator-barashev-grigoriy.git
cd cpp-calculator-barashev-grigoriy
git switch -c feature/multiplication
```

CMD:

```bat
cd /d "%UniversityGithub%"
git clone https://github.com/Flovwvers-students/cpp-calculator-barashev-grigoriy.git
cd cpp-calculator-barashev-grigoriy
git switch -c feature/multiplication
```

Linux/macOS:

```sh
mkdir -p "$HOME/github-training"
cd "$HOME/github-training"
git clone https://github.com/Flovwvers-students/cpp-calculator-barashev-grigoriy.git
cd cpp-calculator-barashev-grigoriy
git switch -c feature/multiplication
```

Если уже клонировали этот репозиторий, откройте его папку, проверьте `git status`, переключитесь `git switch main`, выполните `git pull --ff-only` и создайте ветку. Не клонируйте поверх существующей папки.

### Готовое решение для первого упражнения

Откройте указанные файлы редактором и замените содержимое. Во всех 65 проектах стартовый калькулятор содержит только сложение и вычитание; умножение добавляете вы.

src/Calculator.hpp:

```cpp
#pragma once
class Calculator {
public:
    int add(int left, int right) const { return left + right; }
    int subtract(int left, int right) const { return left - right; }
    int multiply(int left, int right) const { return left * right; }
};
```

src/main.cpp:

```cpp
#include <iostream>
#include "Calculator.hpp"
int main() {
    Calculator calculator;
    int left = 5;
    int right = 3;
    int product = calculator.multiply(left, right);
    std::cout << "Calculator\n";
    std::cout << left << " - " << right << " = " << calculator.subtract(left, right) << '\n';
    std::cout << left << " + " << right << " = " << calculator.add(left, right) << '\n';
    std::cout << left << " * " << right << " = " << product << '\n';
}
```

### Сборка и запуск из корня проекта

PowerShell:

```powershell
New-Item -ItemType Directory -Force out | Out-Null
g++ -std=c++17 -Wall -Wextra -pedantic src/main.cpp -o out/calculator.exe
.\out\calculator.exe
```

CMD:

```bat
if not exist out mkdir out
g++ -std=c++17 -Wall -Wextra -pedantic src/main.cpp -o out/calculator.exe
out\calculator.exe
```

Linux/macOS:

```sh
mkdir -p out
g++ -std=c++17 -Wall -Wextra -pedantic src/main.cpp -o out/calculator
./out/calculator
```

На macOS C++ используйте `clang++` вместо `g++`. Выполняйте запуск только после успешной сборки, чтобы не проверить старый исполняемый файл.

Ожидается:

```text
Calculator
5 - 3 = 2
5 + 3 = 8
5 * 3 = 15
```

Проверьте также 0 и отрицательное число: временно поменяйте left/right в Main, соберите и запустите, затем верните 5/3 и повторите сборку. Не проверяйте огромные значения: в Java int переполняется, в C++ переполнение знакового int не определено.

### Commit и push

Во всех оболочках одинаково:

```sh
git status
git diff
git add src/Calculator.hpp src/main.cpp
git commit -m "Add multiplication"
git push -u origin feature/multiplication
```

В `git status` не должны появиться out и исполняемые файлы: они исключены `.gitignore`. В коммит добавляйте только исходники.

## 7. Разработчик: открыть Pull Request

1. На GitHub откройте **ваш рабочий репозиторий** → **Compare & pull request** (или Pull requests → New pull request).
2. Убедитесь: `base: main`, `compare: feature/multiplication`, организация `Flovwvers-students`.
3. Заголовок: `Добавить умножение`. Описание (замените номер):

```markdown
Closes #1

## Что сделано
Добавлены multiply и вывод примера умножения.

## Проверка
Проект собран и запущен; 5*3=15, 0*7=0, -2*3=-6.
Сложение и вычитание сохранены.

## Ограничения
Переполнение не обрабатывается, как оговорено в Issue.
```

4. В **Reviewers** выберите согласованного с командой ревьюера, а не себя и не аналитика.
5. Нажмите **Create pull request**. Передайте ревьюеру ссылку. Не нажимайте Merge до проверки.

## 8. Ревьюер: проверить и дать обратную связь

1. Откройте PR, затем Issue, затем **Files changed**. Сверьте каждый критерий приёмки.
2. Проверьте, что метод действительно умножает, нет удалённых операций, нет out/бинарных файлов и изменений вне задачи.
3. Для проверки на своём компьютере клонируйте этот репозиторий в отдельную папку, выполните `git fetch origin`, `git switch --track origin/feature/multiplication`. Если локальная ветка уже есть, `git switch feature/multiplication`, затем `git pull --ff-only`.
4. Соберите и запустите по разделу 6. Повторите проверки 5/3, 0/7, -2/3. Временные изменения после проверки верните редактором; не отправляйте их от лица разработчика.
5. На вкладке Files changed нажмите плюс рядом с изменённой строкой и **Start a review**. Комментарий должен объяснять наблюдение. Например: «multiply возвращает произведение; переполнение не входит в критерии задачи».
6. Нажмите **Review changes**. Если всё выполнено — **Approve**, текст: «Калькулятор теперь умножает целые числа. 5 × 3 = 15; сложение и вычитание сохранены. Проверены ноль и отрицательное число». Затем **Submit review**.

### Обязательная практика доработки

Чтобы каждый разработчик научился исправлять замечания, перед финальным одобрением ревьюер отправляет **Request changes** с учебным запросом: «Переименуйте product в multiplicationResult, чтобы имя точнее описывало значение». Это упражнение на процесс; короткое имя само по себе не ошибка.

Разработчик заменяет оба употребления product в Main на multiplicationResult, повторяет сборку, затем выполняет одинаково во всех оболочках:

```sh
git diff
git add src/main.cpp
git commit -m "Clarify multiplication result name"
git push
```

Новый коммит попадает в **тот же PR**. Разработчик отвечает на комментарий и нажимает **Re-request review**. Ревьюер проверяет новый diff, снова запускает программу, отмечает обсуждение **Resolve conversation**, затем отправляет **Approve**. Не одобряйте автоматически только потому, что появился новый коммит.

## 9. Merge, закрытие Issue и уборка

1. Ревьюер открывает Conversation: все обязательные условия должны быть выполнены.
2. Нажимает **Merge pull request → Confirm merge** (если доступен Squash and merge, он тоже допустим).
3. Удаляет удалённую ветку через **Delete branch**.
4. Аналитик проверяет Issue: должно стать **Closed** после merge в main благодаря `Closes #номер`. Если этого не произошло, проверьте ссылку и номер и закройте задачу после проверки результата.
5. Разработчик выполняет:

```sh
git switch main
git pull --ff-only
git fetch --prune
git branch -d feature/multiplication
git log --oneline --graph --all
```

После squash Git иногда отказывается удалить локальную ветку через `-d`. Сначала убедитесь по GitHub и diff, что вся работа вошла в main; только тогда можно удалить конкретную учебную ветку через `git branch -D feature/multiplication`. Не удаляйте ветку с несохранённой работой.

Если push отклонён из-за чужих изменений, сначала `git fetch`, прочитайте сообщение, согласуйте изменения с преподавателем. Не используйте force-push. При конфликте в PR разработчик в своей ветке делает `git fetch origin`, `git merge origin/main`, исправляет отмеченные участки, собирает программу, делает commit и push; затем нужна новая проверка.

## 10. Чек-лист завершения

- [ ] Как аналитик создал понятное Issue и назначил разработчика в своём репозитории.
- [ ] Как разработчик создал ветку, собрал проект, сделал commit/push, открыл PR, исправил замечание.
- [ ] Как ревьюер проверил чужой PR, оставил review, запросил исправление, одобрил и слил.
- [ ] В каждом репозитории умножение в main, Issue закрыто, исходники сохранены.

Перед выходом из университетской сессии выполните `git status`, сохраните нужные изменения коммитом и отправьте свою рабочую ветку через `git push`. Проверьте коммит на GitHub. При первом использовании личного диска после повторного входа убедитесь, что папка проекта и `.git` сохранились. Не удаляйте локальную работу при ошибке сети. После входа повторите выбор диска, `GIT_CONFIG_GLOBAL`, проверку программ и при необходимости авторизацию/диагностику прокси. Не считайте браузерные настройки сохранёнными автоматически.

Ориентир на 90 минут: подготовка/приглашения 15; Issue 10; разработка 20; PR и review 15; доработка и merge 20; разбор 10. Установку компиляторов лучше сделать заранее.

## 11. Второй этап: без готового решения

Преподаватель выдаёт новую задачу, например «Добавить целочисленное деление». Аналитик сам определяет поведение при нуле и отрицательных числах, разработчик реализует, ревьюер проверяет. Сохраните Issue → ветка → PR → review → merge; готовые исходники и текст Issue больше не выдаются.

## 12. Для преподавателя

Подготовлено по одному именному репозиторию на студента: 52 для Java (М3), 13 для C++ (М2). Файл students-repositories.csv связывает ФИО, группу, известный логин GitHub и URL. Имена и фамилии транслитерированы; восемь записей содержали только инициалы, они сохранены без угадывания. Посещаемость, оценки, телефоны и почта старост в репозитории не загружаются.

На этапе подготовки **никого не приглашать и не назначать автоматически**: ни collaborators, ни исполнителей Issue, ни ревьюеров PR. Таблица не назначает студентам команду. Все проекты Java одинаковы между собой; все проекты C++ одинаковы между собой. Стартовый проект не содержит готового умножения.

Когда получите логин студента, добавьте его **только в его именной репозиторий**: Settings → Collaborators and teams → Add people → логин → Admin. Дождитесь принятия приглашения. После этого студент сам добавляет выбранных разработчика и ревьюера с Write. Если приглашения ограничены политикой организации, сначала оформите членство нужных людей; управление учебной командой в репозитории остаётся у студента.

Рекомендуемая защита main: обязательный PR, одно чужое одобрение, повторный review после нового push, разрешение обсуждений, запрет удаления и force-push. Студентам объясните, что Admin выдаётся для сбора команды, а не для отключения правил. Доступность защиты зависит от плана и видимости репозитория. Не считайте ветку защищённой, если правило не включилось.

Перед парой проверьте с одной реальной тройкой: владелец учебного репозитория видит Add people, команда принимает приглашения, разработчик отправляет feature-ветку, ревьюер проверяет и сливает PR, Issue закрывается после merge.

## 13. Частые затруднения

| Симптом | Решение |
|---|---|
| Нет нужного Assignee/Reviewer | Проверить логин, принятие приглашения и права в конкретном репозитории |
| Нет Compare & pull request | Проверить успешный push ветки; открыть Pull requests → New pull request |
| Нет Merge / merge заблокирован | Прочитать причину: review, обсуждения, конфликт или права; исправить причину |
| main отклоняет push | Работать в feature-ветке и создать PR |
| javac/g++ не найден | Проверить установку, Path и перезапуск терминала |
| destination path already exists | Открыть уже клонированную папку; не удалять её автоматически |
| Непонятный timeout/407/сертификат | Выполнить раздел 4 и передать преподавателю ошибку без секретов |

## Источники для настроек

- [Git: http.proxy и параметры по URL](https://git-scm.com/docs/git-config).
- [Microsoft: netsh winhttp](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/netsh-winhttp).
- [GitHub: роли репозитория](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).
- [GitHub: rulesets и доступность](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).

## 14. Прокси на личном ноутбуке: Linux и macOS

На этих системах прокси нужен только если этого требует ваша сеть. Установка, сборка и обычная работа с Git описаны выше. Сначала `git ls-remote --heads https://github.com/git/git.git`; если сеть работает, пропустите настройку прокси. Адрес `proxy.university.example:8080` в примерах замените реальным. PAC-файл не является адресом прокси. Пароли не сохраняйте; ошибки сертификатов не обходите отключением TLS.

### Получить текущие настройки

**Linux/macOS (bash/zsh):**

```sh
env | grep -iE '^(http_proxy|https_proxy|all_proxy|no_proxy)='
git config --show-origin --get-regexp '.*proxy.*'
git config --get-urlmatch http.proxy https://github.com
curl -I --connect-timeout 15 https://github.com
```

### Системные настройки macOS

**Дополнительно macOS:**

```sh
scutil --proxy
networksetup -listallnetworkservices
networksetup -getwebproxy "Wi-Fi"
networksetup -getsecurewebproxy "Wi-Fi"
networksetup -getautoproxyurl "Wi-Fi"
```

### Системные настройки Linux GNOME

**Дополнительно Linux с GNOME (если установлен gsettings):**

```sh
gsettings get org.gnome.system.proxy mode
gsettings get org.gnome.system.proxy.http host
gsettings get org.gnome.system.proxy.http port
gsettings get org.gnome.system.proxy.https host
gsettings get org.gnome.system.proxy.https port
gsettings get org.gnome.system.proxy autoconfig-url
```

### Проверить прокси на один запуск

**Linux/macOS:**

```sh
git -c http.proxy="http://proxy.university.example:8080" ls-remote --heads https://github.com/git/git.git
```

### Сохранить прокси только GitHub

**Linux/macOS:**

```sh
git config --global http.https://github.com.proxy "http://proxy.university.example:8080"
git config --get-urlmatch http.proxy https://github.com
```

### Альтернатива: переменные текущей сессии

**Linux/macOS:**

```sh
export http_proxy='http://proxy.university.example:8080'
export https_proxy='http://proxy.university.example:8080'
```

### Убрать добавленные настройки

**Linux/macOS:**

```sh
git config --global --unset-all http.https://github.com.proxy
unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY
```

Подставьте точное имя активной службы из списка вместо `Wi-Fi`. В `scutil --proxy` ищите `HTTPEnable`, `HTTPProxy`, `HTTPPort`, `HTTPSProxy`, `HTTPSPort`, `ProxyAutoConfigURLString`.

В Linux нет единого системного прокси для всех окружений. На KDE и сервере уточните настройки сети у администратора.

Удаляйте только добавленные вами настройки. Общий `http.proxy`, `ALL_PROXY` и `NO_PROXY` проверяются отдельно; источник покажет `git config --show-origin --get-regexp ".*proxy.*"`. Диагностика 407, PAC и сертификатов — раздел 4.5.
