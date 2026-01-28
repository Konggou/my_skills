#ifndef APPSERVICE_H
#define APPSERVICE_H

#include <QObject>
#include <QString>

/**
 * Generic backend service.
 * Encapsulates business logic and/or external API calls.
 * Communicates via Qt signals (and optionally callbacks).
 */
class AppService : public QObject
{
    Q_OBJECT

public:
    explicit AppService(QObject *parent = nullptr);

    void DoWork(const QString &input);

signals:
    void WorkCompleted(bool success, const QString &result);
    void ErrorOccurred(const QString &message);

private:
    void OnWorkDone(bool ok, const QString &msg);
};

#endif // APPSERVICE_H
