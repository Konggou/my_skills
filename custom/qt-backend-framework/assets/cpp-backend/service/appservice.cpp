#include "appservice.h"

AppService::AppService(QObject *parent)
    : QObject(parent)
{
}

void AppService::DoWork(const QString &input)
{
    (void)input;
    // Placeholder: run business logic or API call, then emit result.
    bool ok = true;
    QString result = "done";
    OnWorkDone(ok, result);
}

void AppService::OnWorkDone(bool ok, const QString &msg)
{
    if (ok)
        emit WorkCompleted(true, msg);
    else
        emit ErrorOccurred(msg);
}
