package com.example.geradordenumeroreal

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.geradordenumeroreal.databinding.ActivityDoacaoBinding

class Doacao : AppCompatActivity() {
    private lateinit var binding: ActivityDoacaoBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityDoacaoBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.voltarBnt.setOnClickListener {

            val voltar = Intent(this, PrimeiraTela::class.java)
            startActivity(voltar)
        }

    }
}
