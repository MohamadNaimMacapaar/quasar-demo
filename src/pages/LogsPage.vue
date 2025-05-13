<template>
  <div class="q-pa-md" style="background: #f7f9fb; min-height: 100vh">
    <!-- Top Category Buttons -->
    <div class="row q-col-gutter-md q-mb-lg">
      <div class="col">
        <q-btn
          class="full-width"
          color="white"
          text-color="primary"
          unelevated
          :class="selectedCategory === 'cs' ? 'category-active' : ''"
          @click="selectedCategory = 'cs'"
        >
          <span class="text-h6">Computer Science</span>
        </q-btn>
      </div>
      <div class="col">
        <q-btn
          class="full-width"
          color="white"
          text-color="primary"
          unelevated
          :class="selectedCategory === 'it' ? 'category-active' : ''"
          @click="selectedCategory = 'it'"
        >
          <span class="text-h6">Information Technology</span>
        </q-btn>
      </div>
      <div class="col">
        <q-btn
          class="full-width"
          color="white"
          text-color="primary"
          unelevated
          :class="selectedCategory === 'is' ? 'category-active' : ''"
          @click="selectedCategory = 'is'"
        >
          <span class="text-h6">Information Security</span>
        </q-btn>
      </div>
    </div>

    <!-- Section Title -->
    <div class="text-h6 text-bold q-mb-md" style="color: #2d3a4a">Recent Logs</div>

    <!-- Logs Table -->
    <q-card flat class="logs-table-card">
      <q-table
        :rows="filteredLogs"
        :columns="columns"
        row-key="logNo"
        hide-bottom
        flat
        class="logs-table"
      >
        <template v-slot:body-cell-action="props">
          <q-td :props="props" class="text-right">
            <q-btn outline color="primary" label="View" size="sm" />
          </q-td>
        </template>
        <template v-slot:body-cell-thesis="props">
          <q-td :props="props">
            <span class="ellipsis" style="max-width: 160px; display: inline-block">{{
              props.row.thesis
            }}</span>
          </q-td>
        </template>
      </q-table>
    </q-card>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const selectedCategory = ref('cs')

const columns = [
  { name: 'logNo', label: 'Log no.', align: 'left', field: 'logNo', sortable: false },
  { name: 'thesis', label: 'Thesis', align: 'left', field: 'thesis', sortable: false },
  { name: 'time', label: 'Time', align: 'left', field: 'time', sortable: false },
  { name: 'status', label: 'Status', align: 'left', field: 'status', sortable: false },
  { name: 'date', label: 'Date', align: 'left', field: 'date', sortable: false },
  { name: 'action', label: '', align: 'right', field: 'action', sortable: false },
]

const logs = [
  {
    logNo: '01.',
    thesis: 'Online Scoring System',
    time: '14:23',
    status: 'Complete',
    date: '11/26/2024',
    category: 'cs',
  },
  {
    logNo: '02.',
    thesis: 'Attendance monitoring',
    time: '15:57',
    status: 'Complete',
    date: '8/4/2024',
    category: 'cs',
  },
  {
    logNo: '03.',
    thesis: 'Online College Enrollment',
    time: '21:01',
    status: 'Complete',
    date: '7/24/2024',
    category: 'cs',
  },
  {
    logNo: '04.',
    thesis: 'School Canteen Voucher System',
    time: '22:56',
    status: 'In Progress',
    date: '12/30/2023',
    category: 'cs',
  },
  {
    logNo: '05.',
    thesis: 'Supporfrog Adventure',
    time: '6:44',
    status: 'In Progress',
    date: '9/5/2023',
    category: 'it',
  },
  {
    logNo: '06.',
    thesis: 'Cemetery Mapping and Info',
    time: '9:23',
    status: 'Complete',
    date: '7/27/2023',
    category: 'it',
  },
  {
    logNo: '07.',
    thesis: 'Book Catalog App',
    time: '18:11',
    status: 'Complete',
    date: '5/21/2023',
    category: 'is',
  },
  {
    logNo: '08.',
    thesis: 'Barcode Technology',
    time: '21:21',
    status: 'Complete',
    date: '2/22/2023',
    category: 'is',
  },
]

const filteredLogs = computed(() => logs.filter((log) => log.category === selectedCategory.value))
</script>

<style scoped>
.category-active {
  background: #e6edfa !important;
  color: #222 !important;
  font-weight: bold;
  border-radius: 16px;
}
.logs-table-card {
  border-radius: 24px;
  background: #fff;
  padding: 16px 0;
}
.logs-table {
  border-radius: 16px;
  background: #fff;
}
.ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
