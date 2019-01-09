class NotificationCallback(Callback):
    def on_train_begin(self):
        self.epoch = 0
    def on_epoch_end(self, metrics):
        val_loss, accuracy = metrics[0], metrics[1]
        message = "Epoch: " + str(self.epoch) + " Val.Loss: " + str(val_loss[0])[0:7] + " Val.Acc: " + str(accuracy)[0:7]
        send_notification(message)
        self.epoch += 1
