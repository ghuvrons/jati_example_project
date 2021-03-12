import Jati

if __name__ == "__main__":
    try:
        Jati = Jati.Jati()
        Jati.addVHost({'localhost': 'localhost'})
        Jati.start()
    except KeyboardInterrupt:
        print("closing")
        Jati.close()