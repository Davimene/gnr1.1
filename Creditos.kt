package com.example.geradordenumeroreal

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.geradordenumeroreal.databinding.ActivityCreditosBinding

class Creditos : AppCompatActivity() {
    private lateinit var binding: ActivityCreditosBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityCreditosBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.voltarBnt.setOnClickListener {

            val voltar = Intent(this, MainActivity::class.java)
            startActivity(voltar)
        }

    }
}
