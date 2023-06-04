<template>
    <div>
        <v-row>
            <v-col align="center">
                <p class="text-h5 mt-10">QRコードを読み込んでください</p>
            </v-col>
        </v-row>
        <QRCode/>
        <v-row>
            <v-col align="center" class="mt-5">
                <v-btn @click="cancel" color="error" class="font-weight-bold">キャンセル</v-btn>
            </v-col>
        </v-row>

    </div>
</template>
<script>
import QRCode from '@/components/QRCode'
export default{
    components:{
        QRCode,
    },
    methods:{
        cancel(){
            this.$router.push('/home')
        }
    }
}
</script>