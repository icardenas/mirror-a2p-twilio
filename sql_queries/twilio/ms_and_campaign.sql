--Messaging Service without campaign and with phone number
--current problem with this ticket https://console.twilio.com/us1/support/tickets?frameUrl=%2Fconsole%2Fsupport%2Ftickets%2F7061439%3F__override_layout__%3Dembed%26bifrost%3Dtrue%26x-target-region%3Dus1
select ms.sid, ms.friendly_name,
       --ms.inbound_method, ms.inbound_request_url,
       ms.us_app_to_person_registered, ms.use_inbound_webhook_on_number,
       tmc.sid,
       tmp.friendly_name, tmp.phone_number, tmp.sms_url, tmp.sms_method
from twilio_management_messagingservice ms
         left join twilio_management_compliance tmc on ms.id = tmc.messaging_service_id
         left join twilio_management_phonenumber tmp on ms.id = tmp.messaging_service_id
where tmc.id is null
  and tmp.id is not null
ORDER BY 2 asc;