# -*- coding: utf-8 -*-
import smtplib
from unittest.mock import MagicMock
from mailer import send


def test_send(monkeypatch):
    smtp_mock = MagicMock()
    smtp_mock.sendmail.return_value = {}

    monkeypatch.setattr(smtplib, 'SMTP', MagicMock(return_value=smtp_mock))

    res = send(
        'john.doe@example.com',
        'john.doe@example.com',
        'topic',
        'body'
    )
    assert res == {}
