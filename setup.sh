cp battery_logger.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable battery_logger.service
systemctl start battery_logger.service
