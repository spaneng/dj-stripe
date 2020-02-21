# Generated by Django 3.1.3 on 2020-11-11 01:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import djstripe.enums
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0008_invoiceitem_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubscriptionSchedule",
            fields=[
                (
                    "djstripe_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                (
                    "livemode",
                    models.BooleanField(
                        blank=True,
                        default=None,
                        help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.",
                        null=True,
                    ),
                ),
                (
                    "created",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="The datetime this object was created in stripe.",
                        null=True,
                    ),
                ),
                (
                    "metadata",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="A set of key/value pairs that you can attach to an object. It can be useful for storing additional information about an object in a structured format.",
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="A description of this object.", null=True
                    ),
                ),
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                (
                    "canceled_at",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="Time at which the subscription schedule was canceled.",
                        null=True,
                    ),
                ),
                (
                    "completed_at",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="Time at which the subscription schedule was completed.",
                        null=True,
                    ),
                ),
                (
                    "current_phase",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="Object representing the start and end dates for the current phase of the subscription schedule, if it is `active`.",
                        null=True,
                    ),
                ),
                (
                    "default_settings",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="Object representing the subscription schedule’s default settings.",
                        null=True,
                    ),
                ),
                (
                    "end_behavior",
                    djstripe.fields.StripeEnumField(
                        enum=djstripe.enums.SubscriptionScheduleEndBehavior,
                        help_text="Behavior of the subscription schedule and underlying subscription when it ends.",
                        max_length=7,
                    ),
                ),
                (
                    "phases",
                    djstripe.fields.JSONField(
                        blank=True,
                        help_text="Configuration for the subscription schedule’s phases.",
                        null=True,
                    ),
                ),
                (
                    "released_at",
                    djstripe.fields.StripeDateTimeField(
                        blank=True,
                        help_text="Time at which the subscription schedule was released.",
                        null=True,
                    ),
                ),
                (
                    "status",
                    djstripe.fields.StripeEnumField(
                        enum=djstripe.enums.SubscriptionScheduleStatus,
                        help_text="The present status of the subscription schedule. Possible values are `not_started`, `active`, `completed`, `released`, and `canceled`.",
                        max_length=11,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        help_text="The customer who owns the subscription schedule.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="schedules",
                        to="djstripe.customer",
                    ),
                ),
                (
                    "djstripe_owner_account",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        help_text="The Stripe Account this object belongs to.",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.account",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "released_subscription",
                    models.ForeignKey(
                        blank=True,
                        help_text="The subscription once managed by this subscription schedule (if it is released).",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="released_schedules",
                        to="djstripe.subscription",
                    ),
                ),
            ],
            options={
                "get_latest_by": "created",
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="subscription",
            name="schedule",
            field=models.ForeignKey(
                blank=True,
                help_text="The schedule associated with this subscription.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscriptions",
                to="djstripe.subscriptionschedule",
            ),
        ),
    ]
