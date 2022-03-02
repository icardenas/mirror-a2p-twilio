--Check if phone number use a post or back url
select *
from twilio_management_phonenumber tmp
where (tmp.sms_url != 'https://api.apploi.com/v1/application_message_sms/get-received' and
       tmp.sms_url not like '%staging%' and lower(tmp.friendly_name) not like  '%staging%')
   or tmp.sms_method != 'GET'
ORDER BY sms_url;
--check if phone number doesn't have a message service
select tmp.phone_number,
       tmp.friendly_name,
       tmp.sms_fallback_method,
       tmp.sms_fallback_url,
       tmp.sms_method,
       tmp.sms_url,
       tmp.status
from twilio_management_phonenumber tmp
where sms_url != 'https://api.apploi.com/v1/application_message_sms/get-received'
  and messaging_service_id is null
order by sms_url;
--Check if Messagign service not use_inbound_webhook_on_number
select tmm.* from twilio_management_phonenumber tmp join twilio_management_messagingservice tmm on tmm.id = tmp.messaging_service_id
where use_inbound_webhook_on_number = true;