select tmm.friendly_name,
       tmm.sid,
       tmp.phone_number,
       tmp.friendly_name,
       tmb.brand_score,
       tmb.brand_type,
       tmb.identity_status,
       a2p.friendly_name
from twilio_management_a2pbrand a2p
         join twilio_management_brandregistration tmb on a2p.id = tmb.a2p_brand_id
         join twilio_management_compliance tmc on tmb.sid = tmc.brand_registration_sid
         join twilio_management_messagingservice tmm on tmc.messaging_service_id = tmm.id
         join twilio_management_phonenumber tmp on tmm.id = tmp.messaging_service_id
--where a2p.friendly_name = 'Apploi Holdings Inc.'
WHERE tmb.brand_type = 'STANDARD'
GROUP BY 1, 2, 3, 4, 5, 6, 7, 8;