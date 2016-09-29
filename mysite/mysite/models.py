from __future__ import unicode_literals
from django.db import models

from django.db import models
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.


class CkKpdHz(models.Model):
    danj_no = models.CharField(primary_key=True, max_length=14)
    danw_id = models.CharField(max_length=11, blank=True)
    riqi_date = models.DateField(blank=True, null=True)
    yew_staff = models.CharField(max_length=10, blank=True)
    tih_way = models.CharField(max_length=2, blank=True)
    chuku_order = models.CharField(max_length=2, blank=True)
    zhix_flg = models.CharField(max_length=2, blank=True)
    shangj_danj_no = models.CharField(max_length=14, blank=True)
    zuoy_state = models.CharField(max_length=2, blank=True)
    jiesuan_type = models.CharField(max_length=20, blank=True)
    boci_no = models.CharField(max_length=20, blank=True)
    tih_way_zh = models.CharField(max_length=2, blank=True)
    guaq_flg = models.CharField(max_length=2, blank=True)
    dayzjbq_flg = models.CharField(max_length=2, blank=True)
    budan_no = models.CharField(max_length=14, blank=True)
    cuowcl_flg = models.CharField(max_length=2, blank=True)
    erji_danw_id = models.CharField(max_length=11, blank=True)
    fafzp_flg = models.CharField(max_length=2, blank=True)
    zengpff_way = models.CharField(max_length=2, blank=True)
    diaod_staff = models.CharField(max_length=10, blank=True)
    keh_notes = models.CharField(max_length=100, blank=True)
    dingd_type = models.CharField(max_length=2, blank=True)
    jianh_way = models.CharField(max_length=2, blank=True)
    xiaos_type = models.CharField(max_length=6)
    peis_type = models.CharField(max_length=20, blank=True)
    tuoy_pay = models.CharField(max_length=20, blank=True)
    buffer_type = models.CharField(max_length=2, blank=True)
    queh_flg = models.CharField(max_length=2, blank=True)
    buh_time = models.DateField(blank=True, null=True)
    yez_id = models.CharField(max_length=20, blank=True)
    shangp_type = models.CharField(max_length=2, blank=True)
    kaip_time = models.DateField(blank=True, null=True)
    jies_time = models.DateField(blank=True, null=True)
    zhuangcd_no = models.CharField(max_length=20, blank=True)
    chongh_flg = models.CharField(max_length=2)
    zancq_no = models.CharField(max_length=11, blank=True)
    waifhdy_flg = models.CharField(max_length=2, blank=True)
    danjxc_side = models.CharField(max_length=1)
    shif_tbj = models.CharField(max_length=2, blank=True)
    yewdj_no = models.CharField(max_length=14, blank=True)
    shuip_type = models.CharField(max_length=4, blank=True)
    fuhdy_rq = models.DateField(blank=True, null=True)
    sf_gxht = models.CharField(max_length=2, blank=True)
    baod_staff = models.CharField(max_length=10, blank=True)
    baogdqr_flg = models.CharField(max_length=2, blank=True)
    qiszcq_no = models.CharField(max_length=11, blank=True)
    zhongzzcq_no = models.CharField(max_length=11, blank=True)
    neifhwc_time = models.DateField(blank=True, null=True)
    waifhwc_time = models.DateField(blank=True, null=True)
    sf_rgsqph = models.CharField(max_length=2, blank=True)
    yaoj_no = models.CharField(max_length=30, blank=True)
    jihwc_flg = models.CharField(max_length=2, blank=True)
    class Meta:
        managed = False
        db_table = 'ck_kpd_hz'
    def __str__(self):
        return self.danj_no
