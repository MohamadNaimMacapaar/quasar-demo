<template>
  <div class="q-pa-md" style="background: #f7f9fb; min-height: 100vh">
    <!-- Group Members Section -->
    <div class="text-h6 text-bold q-mb-md" style="color: #2d3a4a">Group Member</div>
    <div class="row items-center q-col-gutter-md q-mb-lg">
      <div class="col-3" v-for="(member, idx) in groupMembers" :key="idx">
        <q-card flat bordered class="member-card">
          <q-card-section>
            <div class="text-caption text-grey-7">Name</div>
            <div class="text-subtitle1 text-weight-medium">{{ member.name }}</div>
            <div class="row q-mt-xs">
              <div class="col">
                <div class="text-caption text-grey-7">Year Level</div>
                <div class="text-body2">{{ member.year }}</div>
              </div>
              <div class="col">
                <div class="text-caption text-grey-7">ID no.</div>
                <div class="text-body2">{{ member.id }}</div>
              </div>
            </div>
            <div class="q-mt-md text-caption text-grey-7">
              Department: <span class="text-weight-medium">{{ member.department }}</span>
            </div>
          </q-card-section>
        </q-card>
      </div>
      <div class="col-auto flex flex-center">
        <q-btn round color="primary" icon="add" size="lg" class="add-btn" @click="addMember" />
      </div>
    </div>

    <!-- Title Section -->
    <div class="text-h6 text-bold q-mb-sm" style="color: #2d3a4a">Title</div>
    <div class="row items-center q-mb-lg">
      <div class="col">
        <q-input
          v-model="title"
          outlined
          dense
          class="title-input"
          placeholder="Enter thesis title"
        />
      </div>
      <div class="col-auto">
        <q-btn
          color="primary"
          class="upload-btn"
          label="Upload File"
          icon="cloud_upload"
          @click="uploadFile"
        />
      </div>
    </div>

    <!-- Description Section -->
    <div class="text-h6 text-bold q-mb-sm" style="color: #2d3a4a">Description</div>
    <q-input
      v-model="description"
      type="textarea"
      outlined
      autogrow
      class="desc-input"
      placeholder="Enter thesis description"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'

const groupMembers = ref([
  {
    name: 'Abdul GGs',
    year: '2021-2022',
    id: '202356735',
    department: 'Computer Science',
  },
  {
    name: 'Mjolnir Rizz',
    year: '2021-2022',
    id: '202356735',
    department: 'Computer Science',
  },
])

const title = ref('CICS Thesis Archive Frontend')
const description = ref(
  `Hello World! This is a sample description for the thesis. It can be as long as you want it to be, and it will automatically grow as you type.`,
)

function addMember() {
  groupMembers.value.push({
    name: '',
    year: '',
    id: '',
    department: '',
  })
}

function uploadFile() {
  // Implement file upload logic here
  alert('Upload File clicked!')
}
</script>

<style scoped>
.member-card {
  border-radius: 16px;
  background: #fff;
}
.add-btn {
  background: #e6edfa !important;
  color: #1976d2 !important;
  box-shadow: 0 2px 8px #1976d233;
}
.title-input {
  border-radius: 16px;
  background: #fff;
  font-weight: bold;
  font-size: 1.1rem;
}
.upload-btn {
  border-radius: 24px;
  font-weight: bold;
  font-size: 1.1rem;
  box-shadow: 0 4px 12px #1976d233;
  padding: 0 24px;
}
.desc-input {
  border-radius: 16px;
  background: #fff;
  font-size: 1rem;
}
</style>
