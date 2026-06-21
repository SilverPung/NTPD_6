# Lab 6: NTPD


## Zadanie 1: Przygotowanie repozytorium z przykładowym modelem ML

Testy zostały napisane porzy użyciu frameworka `pytest` i znajdują się w pliku `tests.py`

![img.png](images/img.png)

po uruchomieniu testów za pomocą polecenia `uv run pytest` otrzymujemy następujący wynik:

![img.png](images/img1.png)

## Zadanie 2: Konfiguracja GitHub Actions do automatycznego testowania

następnie został napisany plik konfiguracyjny `test.yml` w katalogu `.github/workflows`, który zawiera definicję workflow do automatycznego testowania naszego modelu ML przy każdym pushu do repozytorium.

![img_1.png](images/img_1.png)

kod został przetestowany lokalnie i działa poprawnie, a następnie został wypchnięty do repozytorium na GitHubie. Po wypchnięciu kodu, GitHub Actions automatycznie uruchomił workflow i wykonał testy.

![img.png](images/img_2.png)

## Zadanie 3: Automatyczne budowanie obrazu Dockera i jego publikacja 
na koniec zosatł stworzony plik `docker.yml` w katalogu `.github/workflows`, który zawiera definicję workflow do automatycznego budowania obrazu Dockera i jego publikacji na Docker Hub przy każdym pushu do repozytorium.
![img.png](images/img_3.png)

po wypchnięciu kodu, GitHub Actions automatycznie uruchomił workflow i zbudował obraz Dockera, a następnie opublikował go w repozytorium.
![img_1.png](images/img_4.png)

![img_2.png](images/img_5.png)