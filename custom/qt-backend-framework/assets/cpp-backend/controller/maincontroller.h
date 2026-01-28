#ifndef MAINCONTROLLER_H
#define MAINCONTROLLER_H

#include <QObject>
#include <QString>

class AppService;
class AppModel;

/**
 * Coordinates UI and backend services.
 * Owns services and models; connects UI signals to service calls and
 * service signals back to UI (or to other layers).
 */
class MainController : public QObject
{
    Q_OBJECT

public:
    explicit MainController(QObject *parent = nullptr);
    ~MainController();

    AppService *GetAppService() const { return m_app_service; }
    AppModel *GetAppModel() const { return m_app_model; }

    void RequestDoWork(const QString &input);

signals:
    void WorkCompleted(bool success, const QString &result);
    void ErrorOccurred(const QString &message);

private slots:
    void OnServiceWorkCompleted(bool success, const QString &result);
    void OnServiceError(const QString &message);

private:
    AppService *m_app_service;
    AppModel *m_app_model;
};

#endif // MAINCONTROLLER_H
