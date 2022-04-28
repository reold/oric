from deta import Deta

deta = Deta("a02xqre5_DeLH6oDuFUEcc3iEyMHzMzddRQPEjkt4")

uploads_drive = deta.Drive("uploads")
uploads_db = deta.Base("uploads")
